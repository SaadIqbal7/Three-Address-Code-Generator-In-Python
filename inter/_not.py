from inter.logical import Logical
from lexer.token import Token
from inter.expr import Expr


"""
Class for NOT logical operator.
NOT is a unary operator but has a lot in common from logical class
so we make NOT inherit from Logical
"""
class NOT(Logical):
	def __init__(self, token: Token, expr2: Expr):
		super().__init__(token, expr2, expr2)

	def jumping(self, t: int, f: int):
		self.expr2.jumping(f, t)

	def to_string(self):
		return f'{self.op.to_string()} {self.expr2.to_string()}'



