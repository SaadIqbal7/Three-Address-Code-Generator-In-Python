from inter.stmt import Stmt


"""
Class for break statement
"""
class Break(Stmt):
	def __init__(self):
		super().__init__()
		if Stmt.Enclosing == None:
			self.error('unclosed break')
		self.stmt: Stmt = Stmt.Enclosing

	def gen(self, b: int, a: int):
		self.emit(f'goto L{self.stmt.after}')



