from lexer.tag import Tag
from lexer.token import Token

class Real(Token):
	def __init__(self, value: int):
		super().__init__(Tag.REAL)
		self.value = value

	def printToken(self):
		print("REAL:", self.value)

	def to_string(self) -> str:
		return f'{self.value}'

