from inter.stmt import Stmt
from inter.expr import Expr
from symbols.type import Type

"""
Class to implement While statement logic.
"""
class While(Stmt):
	def __init__(self):
		super().__init__()
		self.expr = None
		self.stmt = None

	def init(self, expr: Expr, stmt: Stmt):		
		self.expr = expr
		self.stmt = stmt

		# Check type of expression
		if self.expr.type != Type.BOOL:
			# Throw error here
			self.expr.error("Boolean required in while expression")

	def gen(self, b: int, a: int):
		# Save label a
		self.after = a
		self.expr.jumping(0, a)
		# label for stmt
		label: int = self.new_label()

		self.emit_label(label)
		self.stmt.gen(label, b)
		self.emit(f'goto L{b}')
	


