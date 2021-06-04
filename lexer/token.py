from lexer.tag import Tag

class Token:
	def __init__(self, tag: int):
		self.tag = tag

	def printToken(self):
		print(Tag.INVERSE_DICT[self.tag], ': ', sep='', end='')

	def to_string(self):
		return Tag.INVERSE_DICT[self.tag]

