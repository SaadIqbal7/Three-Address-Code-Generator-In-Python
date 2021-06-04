from lexer._lexer import Lexer
from lexer.token import Token
from lexer.tag import Tag
from lexer.num import Num
from lexer.word import Word
from symbols.env import Env
from symbols.type import Type
from symbols.array import Array
from inter.stmt import Stmt
from inter.id import Id
from inter.seq import Seq
from inter._if import If
from inter._else import Else
from inter._while import While
from inter._do import Do
from inter._break import Break
from inter.set import Set
from inter.set_elem import SetElem
from inter.expr import Expr
from inter._or import OR
from inter._and import AND
from inter._not import NOT
from inter.rel import Rel
from inter.arith import Arith
from inter.unary import Unary
from inter.constant import Constant
from inter.access import Access


class Parser:

	def __init__(self, lexer: Lexer):
		# Lexical analyzer for thir parser
		self.lexer: Lexer = lexer
		# Look ahead token
		self.look: Token = None
		# Current symbol table
		self.top: Env = None
		# Storage used for declarations
		# Used to assign memory address to variables
		self.used = 0

		# Start scanning
		self.move()

	def error(self, s:str):
		raise Exception(s)

	def move(self):
		# Move forward and take next token
		self.look = self.lexer.scan()

	def match(self, t: int):
		if self.look.tag == t:
			self.move()
		else:
			self.error("syntax error")
			pass

	# Runs the parser
	def program(self):
		# Parse the input stream and build syntax tree
		s: Stmt = self.block()
		# Generate intermediate code
		begin: int = s.new_label()
		after: int = s.new_label()

		s.emit_label(begin)
		s.gen(begin, after)
		s.emit_label(after)

	# A block is statments enclosed within { declared stmts }
	def block(self) -> Stmt:
		self.match(Tag.CURLY_BRACKETS_OPEN)
		# Hold the previous symbol table
		savedEnv: Env = self.top
		self.top = Env(self.top)
		self.decls()
		s: Stmt = self.stmts()
		self.match(Tag.CURLY_BRACKETS_CLOSE)
		self.top = savedEnv
		return s

	# Declared variables are represented by identifiers
	# and these identifiers make up the symbol table
	def decls(self):
		# BASIC tag is the tag given to all the variables of type
		# INT, FLOAT, CHAR, BOOL. So, BASIC tag represents that an identifier
		while self.look.tag == Tag.BASIC:
			# Get the type of token
			# Type can be FLOAT, CHAR. INT, BOOL or Array
			_type: Type = self.type()
			# The identifier is a Word so, downcast lookahead token to Word
			token: Word = self.look
			# After the type, the next token should be an identifier and
			# the token after that should be a semi colon
			self.match(Tag.ID)
			self.match(Tag.SEMICOLON)
			# Create Id for variable name
			# Give it token, type and assign it relative address
			_id = Id(token, _type, self.used)
			# Put identifier in symbol table
			self.top.put(token, _id)
			# Update the address pointer
			# Move pointer forward by the width the variable occupies
			self.used += _type.width

	# Returns type of the current token
	def type(self):
		# Cast current token to type
		_type: Type = self.look # Check type when look.tag == Tag.BASIC
		# Now match the type
		self.match(Tag.BASIC)
		# Check if its a basic type of array
		if self.look.tag != Tag.SQR_BRACKET_OPEN:
			return _type # Return basic type
		else:
			return self.dims(_type) # Return array type

	def dims(self, _type: Type):
		self.match(Tag.SQR_BRACKET_OPEN)
		token: Num = self.look
		# Match the number b/w brackets
		self.match(Tag.NUM)
		# Match closing bracket
		self.match(Tag.SQR_BRACKET_CLOSE)
		# Check if another opening square bracket is encountered
		# this means a multi-dimensional array
		if self.look.tag == Tag.SQR_BRACKET_OPEN:
			# Call dims again
			_type = self.dims(_type)

		# Return array type
		return Array(_type, token.value)

	def stmts(self) -> Stmt:
		if self.look.tag == Tag.CURLY_BRACKETS_CLOSE:
			return Stmt.Null
		else:
			return Seq(self.stmt(), self.stmts())

	def stmt(self) -> Stmt:
		expr: Expr = None
		s: Stmt = None
		s1: Stmt = None
		s2: Stmt = None
		# Save enclosing loop for breaks
		savedStmt: Stmt = None

		if self.look.tag == Tag.SEMICOLON:
			# Move to next statment
			self.move()
			# Return NULL statement
			return Stmt.Null
		elif self.look.tag == Tag.IF:
			# Match with IF (this will always run)
			self.match(Tag.IF)
			# Check for open paranthesis '('
			self.match(Tag.PARANTHESIS_OPEN)
			# Check for boolean expression
			# boolean expression could be a series of ANDs ORs NOTs
			expr = self.bool()
			# Check for close paranthesis ')'
			self.match(Tag.PARANTHESIS_CLOSE)
			# Get sequence of statements for the code below IF
			# and execute them.
			s1 = self.stmt()
			# Check if ELSE is not encountered
			if self.look.tag != Tag.ELSE:
				# Return IF block
				return If(expr, s1)
			# Match with ELSE statement (this will always run)
			self.match(Tag.ELSE)
			# Get sequence of statements for else block
			s2 = self.stmt()
			# Return IF ELSE block
			return Else(expr, s1, s2)
		elif self.look.tag == Tag.WHILE:
			# Create while node
			while_node: While = While()
			savedStmt = Stmt.Enclosing
			Stmt.Enclosing = while_node
			# Match with WHILE statement (this will always work)
			self.match(Tag.WHILE)
			# Check for open paranthesis '('
			self.match(Tag.PARANTHESIS_OPEN)
			# Check for boolean expression
			# boolean expression could be a series of ANDs ORs NOTs
			expr = self.bool()
			# Check for close paranthesis ')'
			self.match(Tag.PARANTHESIS_CLOSE)
			# Get sequence of statements for while block
			s1 = self.stmt()
			# Initialize while loop with while loop expression and statements
			while_node.init(expr, s1)
			# Reset Stmt.Enclosing
			Stmt.Enclosing = savedStmt
			return while_node
		elif self.look.tag == Tag.DO:
			# Create while node
			do_node: Do = Do()
			savedStmt = Stmt.Enclosing
			Stmt.Enclosing = do_node
			# Match with DO statement (this will always work)
			self.match(Tag.DO)
			# Get sequence of statements for do block
			s1 = self.stmt()
			# Check for while statement
			self.match(Tag.WHILE)
			# Check for open paranthesis '('
			self.match(Tag.PARANTHESIS_OPEN)
			# Check for boolean expression
			# boolean expression could be a series of ANDs ORs NOTs
			expr = self.bool()
			# Check for close paranthesis ')'
			self.match(Tag.PARANTHESIS_CLOSE)
			# Check for semicolon
			self.match(Tag.SEMICOLON)
			# Initialize do loop with do loop statements and expression
			do_node.init(s1, expr)
			# Reset Stmt.Enclosing
			Stmt.Enclosing = savedStmt
			return do_node
		elif self.look.tag == Tag.BREAK:
			# Match with BREAK statement (this will always work)
			self.match(Tag.BREAK)
			# Check for semicolon
			self.match(Tag.SEMICOLON)
			return Break()
		elif self.look.tag == Tag.CURLY_BRACKETS_OPEN:
			# Start of new block b/w '{' and '}'
			return self.block()
		else:
			return self.assign()

	def assign(self) -> Stmt:
		stmt: Stmt = None
		token: Token = self.look
		# Match ID (this will always work)
		self.match(Tag.ID)
		# Get identifier from Symbol table
		_id: Id = self.top.get(token)

		# Check if identifier is not found in symbol table
		if _id == None:
			self.error(f'{token.to_string()} undeclared')

		# Check for assignment operator
		if self.look.tag == Tag.ASSIGN:
			# Move and read the constant or statement
			self.move()
			# Set element for single variable id = E
			stmt = Set(_id, self.bool())
		else: # When array brackets is encountered after indentifier array[20]
			access: Access = self.offset(_id)
			# Check for assignment operator
			self.match(Tag.ASSIGN)
			# Set elements for array array = E
			stmt = SetElem(access, self.bool())
		# Match semicolon
		self.match(Tag.SEMICOLON)
		return stmt

	def bool(self) -> Expr:
		expr: Expr = self.join()
		# Check while tag is OR
		while self.look.tag == Tag.OR:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			expr = OR(token, expr, self.join())
		return expr

	def join(self) -> Expr:
		expr: Expr = self.equality()
		# Check while tag is AND
		while self.look.tag == Tag.AND:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			expr = AND(token, expr, self.equality())
		return expr

	def equality(self) -> Expr:
		expr: Expr = self.rel()

		# Check while tag is AND
		while self.look.tag == Tag.EQ or self.look.tag == Tag.NE:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			expr = Rel(token, expr, self.rel())
		return expr

	def rel(self) -> Expr:
		expr: Expr = self.expr()

		# Check while tag is AND
		if self.look.tag == Tag.LT or self.look.tag == Tag.GT or self.look.tag == Tag.LE or self.look.tag == Tag.GE:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			return Rel(token, expr, self.expr())
		else:
			return expr

	def expr(self) -> Expr:
		expr: Expr = self.term()

		# Check while tag is AND
		while self.look.tag == Tag.PLUS or self.look.tag == Tag.MINUS:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			expr = Arith(token, expr, self.term())
		return expr

	def term(self) -> Expr:
		expr: Expr = self.unary()
		# Check while tag is AND
		while self.look.tag == Tag.MULTIPLY or self.look.tag == Tag.DIVIDE:
			token: Token = self.look
			# Move forward
			self.move()
			# Create OR expression
			expr = Arith(token, expr, self.unary())
		return expr

	def unary(self) -> Expr:
		if self.look.tag == Tag.MINUS:
			# Move forward
			self.move()
			return Unary(Word.MINUS, self.unary())
		elif self.look.tag == Tag.NOT:
			token: Token = self.look
			# Move forward
			self.move()
			NOT(token, self.unary())
		else:
			return self.factor()

	def factor(self) -> Expr:
		expr: Expr = None
		if self.look.tag == Tag.PARANTHESIS_OPEN:
			# Move forward
			self.move()
			# Read boolean expression b/w paranthesis
			expr = self.bool()
			self.match(Tag.PARANTHESIS_CLOSE)
			return expr
		elif self.look.tag == Tag.NUM:
			# Create constant with the number
			expr = Constant(token=self.look, p=Type.INT)
			# Move forward
			self.move()
			return expr
		elif self.look.tag == Tag.REAL:
			# Create constant with the number
			expr = Constant(token=self.look, p=Type.FLOAT)
			# Move forward
			self.move()
			return expr
		elif self.look.tag == Tag.TRUE:
			# Create constant with the number
			expr = Constant.TRUE
			# Move forward
			self.move()
			return expr
		elif self.look.tag == Tag.FALSE:
			# Create constant with the number
			expr = Constant.FALSE
			# Move forward
			self.move()
			return expr
		elif self.look.tag == Tag.ID:
			s: str = self.look.to_string()
			# Get identifier from symbol table
			_id: Id = self.top.get(self.look)
			# Check if identifier was not found in symbol table
			if _id == None:
				self.error(f'{s} undeclared')
			# Move forward
			self.move()
			if self.look.tag != Tag.SQR_BRACKET_OPEN:
				return _id
			else:
				return self.offset(_id)
		else:
			self.error('syntax error')
			return expr

	def offset(self, _id: Id) -> Access:
		i: Expr = None
		w: Expr = None
		t1: Expr = None
		t2: Expr = None
		loc: Expr = None

		_type: Type = _id.type
		self.match(Tag.SQR_BRACKET_OPEN)
		i = self.bool()
		self.match(Tag.SQR_BRACKET_CLOSE)
		_type_arr: Array = _type
		_type_arr = _type_arr.of
		w = Constant(value=_type_arr.width)
		t1 = Arith(Token(Tag.MULTIPLY), i, w)
		loc = t1

		while self.look.tag == Tag.SQR_BRACKET_OPEN:
			self.match(Tag.SQR_BRACKET_OPEN)
			i = self.bool()
			self.match(Tag.SQR_BRACKET_CLOSE)
			_type_arr = _type_arr.of
			w = Constant(value=_type_arr.width)
			t1 = Arith(Token(Tag.MULTIPLY), i, w)
			t2 = Arith(Token(Tag.PLUS), loc, t1)
			loc = t2

		return Access(_id, loc, _type_arr)

