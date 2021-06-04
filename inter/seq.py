from inter.stmt import Stmt

'''
Sequence class implements a sequence of statements
'''
class Seq(Stmt):

	def __init__(self, s1: Stmt, s2: Stmt):
		super().__init__()
		self.s1 = s1
		self.s2 = s2

	def gen(self, b: int, a: int):
		if self.s1 == Stmt.Null:
			self.s2.gen(b, a)
		elif self.s2 == Stmt.Null:
			self.s1.gen(b, a)
		else:
			label: int = self.new_label()
			self.s1.gen(b, label)
			self.emit_label(label)
			self.s2.gen(label, a)

