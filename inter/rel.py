from inter.logical import Logical
from lexer.token import Token
from symbols.array import Array
from inter.expr import Expr
from symbols.type import Type

"""
Class for implementing relational operators > < >= etc.
"""
class Rel(Logical):
	def __init__(self, token: Token, expr1: Expr, expr2: Expr):
		super().__init__(token, expr1, expr2)

	
	def check(self, p1: Type, p2: Type) -> Type:
		if type(p1) == Array or type(p2) == Array:
			return None
		elif p1 == p2:
			return Type.BOOL
		else:
			return None

	def jumping(self, t: int, f: int):
		a: Expr = self.expr1.reduce()
		b: Expr = self.expr2.reduce()

		s: str = f'{a.to_string()} {self.op.to_string()} {b.to_string()}'
		self.emitjumps(s, t, f)

	



