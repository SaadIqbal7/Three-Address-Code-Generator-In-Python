from lexer.tag import Tag
from lexer.token import Token

class Num(Token):
	def __init__(self, value: int):
		super().__init__(Tag.NUM)
		self.value = value

	def printToken(self):
		print("NUM:", self.value)

	def to_string(self) -> str:
		return f'{self.value}'
