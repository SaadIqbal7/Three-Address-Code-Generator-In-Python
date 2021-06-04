from inter.logical import Logical
from lexer.token import Token
from inter.expr import Expr


"""
Class for AND logical operator
"""
class AND(Logical):
	def __init__(self, token: Token, expr1: Expr, expr2: Expr):
		super().__init__(token, expr1, expr2)

	def jumping(self, t: int, f: int):
		label: int = f if f != 0 else self.new_label()
		self.expr1.jumping(0, label)
		self.expr2.jumping(t, f)

		if f == 0:
			self.emit_label(label)


