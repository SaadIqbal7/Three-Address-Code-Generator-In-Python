from inter.stmt import Stmt
from inter.id import Id
from inter.expr import Expr
from symbols.type import Type
from inter.access import Access
from symbols.array import Array

'''
Class SetElem implements assignments to an array element
'''
class SetElem(Stmt):
	def __init__(self, access: Access, expr: Expr):
		super().__init__()
		self.array = access.array
		self.index = access.index
		self.expr = expr

		# Check if type of left identifier matches
		# with the type of expression on the right
		if self.check(access.type, self.expr.type) == None:
			self.error('type error')

	def check(self, p1: Type, p2: Type) -> Type:
		if type(p1) == Array or type(p2) == Array:
			return None
		elif p1 == p2:
			return p2
		elif Type.is_numeric(p1) and Type.is_numeric(p2):
			return p2
		else:
			return None

	def gen(self, b: int, a: int):
		s1: str = self.index.reduce().to_string()
		s2: str = self.expr.reduce().to_string()
		self.emit(f'{self.array.to_string()} [ {s1} ] = {s2}')



