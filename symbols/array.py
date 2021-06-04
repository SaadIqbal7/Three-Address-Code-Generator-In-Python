from symbols.type import Type
from lexer.tag import Tag

class Array(Type):
	def __init__(self, of: Type, size: int=1):
		super().__init__("[]", Tag.INDEX, size * of.width)

		# Array of size 'size' and of type 'of'
		self.size = size
		self.of = of

	def to_string(self):
		return f'[{self.size}] {self.of.to_string()}'
		