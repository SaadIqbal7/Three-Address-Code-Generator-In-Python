from inter.stmt import Stmt
from inter.expr import Expr
from symbols.type import Type

"""
Class to implement IF statement logic.
if (Expr) Stmt
"""
class If(Stmt):
	def __init__(self, expr: Expr, stmt: Stmt):
		super().__init__()
		self.expr = expr
		self.stmt = stmt

		# Check type of expression
		if self.expr.type != Type.BOOL:
			# Throw error here
			self.expr.error("Boolean required in if expression")

	def gen(self, b: int, a: int):
		# Label for the code for stmt
		label: int = self.new_label()
		# Continue with statment is expr is true
		# else move to label a if expr is false
		self.expr.jumping(0, a)
		self.emit_label(label)
		self.stmt.gen(label, a)

	

