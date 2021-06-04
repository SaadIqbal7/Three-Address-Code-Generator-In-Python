from inter.node import Node

class Stmt(Node):

	@classmethod
	def static_variables(cls):
		cls.Null: Stmt = Stmt()
		# Used for break stmt
		cls.Enclosing: Stmt = Stmt.Null

	def __init__(self):
		super().__init__()
		self.after: int = 0

	def gen(self, b: int, a: int):
		return

# Initialize static variables
Stmt.static_variables()
