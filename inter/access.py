from inter.op import Op
from inter.id import Id
from inter.expr import Expr
from symbols.type import Type
from lexer.tag import Tag
from lexer.word import Word


class Access(Op):
	def __init__(self, _id: Id, index: Expr, p: Type):
		super().__init__(Word("[]", Tag.INDEX), p)
		self.array = _id
		self.index = index

	def gen(self):
		return Access(self.array, self.index.reduce(), self.type)

	def jumping(self, t: int, f: int):
		self.emitjumps(self.reduce().to_string(), t, f)

	def to_string(self):
		return f'{self.array.to_string()} [ {self.index.to_string()} ]'




