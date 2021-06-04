from inter.stmt import Stmt
from inter.id import Id
from inter.expr import Expr
from symbols.type import Type


'''
Class Set implements assignment of expression on the right to the 
indentifier on the left
'''
class Set(Stmt):
	def __init__(self, i: Id, expr: Expr):
		super().__init__()
		self.id = i
		self.expr = expr

		# Check if type of left identifier matches 
		# with the type of expression on the right
		if self.check(self.id.type, self.expr.type) == None:
			self.error('type error')
	
	def check(self, p1: Type, p2: Type) -> Type:
		if Type.is_numeric(p1) and Type.is_numeric(p2):
			return p2
		elif p1 == Type.BOOL and p2 == Type.BOOL:
			return p2
		else:
			return None

	def gen(self, b: int, a: int):
		self.emit(f'{self.id.to_string()} = {self.expr.gen().to_string()}')


