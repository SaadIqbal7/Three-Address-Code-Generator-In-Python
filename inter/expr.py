from inter.node import Node
from lexer.token import Token
from symbols.type import Type

'''
A class for Expression which has an operator and a type
'''
class Expr(Node):
	def __init__(self, op: Token, p: Type):
		super().__init__()
		self.op = op
		self.type = p

	# Function that represents the right side of the expression
	# e.g.
	# E = E1 + E2
	# so, gen returns E1 + E2
	# As we want to return the address of the expression, that is why
	# we are returning self object
	def gen(self):
		return self

	# Function to compute or "reduce" the left side of the expression
	# e.g.
	# E = E1 + E2
	# so, reduce temporary value for E1 + E2 or and identifier
	# As we want to return the address of the expression, that is why
	# we are returning self object
	def reduce(self):
		return self

	def to_string(self) -> str:
		return self.op.to_string()

	def jumping(self, t: int, f: int):
		self.emitjumps(self.to_string(), t, f)

	def emitjumps(self, s: str, t: str, f: str):
		if t != 0 and f != 0:
			self.emit(f'if {s} goto L{t}')
			self.emit(f'goto L{f}')

		if t != 0:
			self.emit(f'if {s} goto L{t}')
		if f != 0:
			self.emit(f'iffalse {s} goto L{f}')

	def to_string(self):
		return self.op.to_string()			


