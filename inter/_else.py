from inter.stmt import Stmt
from inter.expr import Expr
from symbols.type import Type

"""
Class to implement Else statement logic.
"""
class Else(Stmt):
	def __init__(self, expr: Expr, stmt1: Stmt, stmt2: Stmt):
		super().__init__()
		self.expr = expr
		self.stmt1 = stmt1
		self.stmt2 = stmt2

		# Check type of expression
		if self.expr.type != Type.BOOL:
			# Throw error here
			self.expr.error("Boolean required in if expression")

	def gen(self, b: int, a: int):
		# label1 for stmt1
		# label2 for stmt2
		label1: int = self.new_label()
		label2: int = self.new_label()
		self.expr.jumping(0, label2) # Move to stmt1 if expr is true

		self.emit_label(label1)
		self.stmt1.gen(label1, a)
		self.emit(f'goto L{a}')
		self.emit_label(label2)
		self.stmt2.gen(label2, a)
	


