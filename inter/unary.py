from inter.op import Op
from lexer.token import Token
from inter.expr import Expr
from symbols.type import Type

class Unary(Op):
	def __init__(self, op: Token, expr: Expr):
		super().__init__(op, None)
		self.expr = expr
		self.type = Type.max(Type.INT, self.expr.type)

		if self.type == None:
			self.error('type error')

	def gen(self):
		return Unary(self.op, self.expr.reduce())

	def to_string(self):
		return f'{self.op.to_string()} {self.expr.to_string()}'

