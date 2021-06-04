from lexer.tag import Tag
from lexer.token import Token

class Hex(Token):
	def __init__(self, s: str):
		super().__init__(Tag.HEX)
		self.s = s

	def printToken(self):
		print("HEX:", self.s)
	
	def to_string(self) -> str:
		return self.s
