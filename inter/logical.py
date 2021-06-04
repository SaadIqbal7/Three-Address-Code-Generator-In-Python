from lexer.token import Token
from inter.expr import Expr
from symbols.type import Type
from inter.temp import Temp

"""
Parent class for logical expressions AND OR NOT.
Take two paramaters for operands expr1 and expr2
and a token to represent the operator
"""

class Logical(Expr):

	def __init__(self, token: Token, expr1: Expr, expr2: Expr):
		super().__init__(token, None)
		self.expr1 = expr1
		self.expr2 = expr2

		# Check type of expressions.
		self.type = self.check(self.expr1.type, self.expr2.type)

		if self.type == None:
			self.error("type error")
	
	def check(self, p1: Type, p2: Type) -> Type:
		if p1 == Type.BOOL and p2 == Type.BOOL:
			return Type.BOOL
		return None

	def gen(self) -> Expr:
		f: int = self.new_label()
		a: int = self.new_label()

		temp: Temp = Temp(self.type)

		self.jumping(0, f)
		self.emit(f'{temp.to_string()} = true')
		self.emit(f'goto L{a}')
		self.emit_label(f)
		self.emit(f'{temp.to_string()} = false')
		self.emit_label(a)

		return temp

	def to_string(self):
		return f'{self.expr1.to_string()} {self.op.to_string()} {self.expr2.to_string()}'




