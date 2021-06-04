from inter.logical import Logical
from lexer.token import Token
from inter.expr import Expr


"""
Class for OR logical operator
"""
class OR(Logical):
	def __init__(self, token: Token, expr1: Expr, expr2: Expr):
		super().__init__(token, expr1, expr2)

	def jumping(self, t: int, f: int):
		label: int = t if t != 0 else self.new_label()
		self.expr1.jumping(label, 0)
		self.expr2.jumping(t, f)

		if t == 0:
			self.emit_label(label)


