from inter.expr import Expr
from lexer.word import Word
from symbols.type import Type


class Temp(Expr):
	count = 0

	def __init__(self, p: Type):
		super().__init__(Word.TEMP, p)
		Temp.count += 1
		self.number = Temp.count

	def to_string(self):
		return f't{self.number}'
