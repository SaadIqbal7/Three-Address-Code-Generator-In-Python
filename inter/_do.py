from inter.stmt import Stmt
from inter.expr import Expr
from symbols.type import Type

"""
Class to implement Do statement logic.
"""
class Do(Stmt):
	def __init__(self):
		super().__init__()
		self.expr = None
		self.stmt = None

	def init(self, stmt: Stmt, expr: Expr):		
		self.stmt = stmt
		self.expr = expr

		# Check type of expression
		if self.expr.type != Type.BOOL:
			# Throw error here
			self.expr.error("Boolean required in while expression")

	def gen(self, b: int, a: int):
		# Save label a
		self.after = a
		# label for stmt
		label: int = self.new_label()

		self.stmt.gen(b, label)
		self.emit_label(label)
		self.expr.jumping(b, 0)
	


