from lexer.tag import Tag
from lexer.word import Word


class Type(Word):

	@classmethod
	def static_variables(cls):
		# Define types
		cls.INT = Type("int", Tag.BASIC, 4)
		cls.FLOAT = Type("float", Tag.BASIC, 8)
		cls.CHAR = Type("char", Tag.BASIC, 1)
		cls.BOOL = Type("bool", Tag.BASIC, 1)

	def __init__(self, s: str, tag: int, w: int):
		super().__init__(s, tag)
		# Width of a data type
		# e.g.
		# 4 bytes for int
		# 1 byte for character
		self.width = w

	# Function for checking if a type is numeric
	@staticmethod
	def is_numeric(p) -> bool:
		if p == Type.INT or p == Type.FLOAT or p == Type.CHAR:
			return True
		return False

	@staticmethod
	def max(p1, p2):
		if not Type.is_numeric(p1) or not Type.is_numeric(p2):
			return None
		elif p1 == Type.FLOAT or p2 == Type.FLOAT:
			return Type.FLOAT
		elif p1 == Type.INT  or p2 == Type.INT:
			return Type.INT
		else:
			return Type.CHAR

	def to_string(self):
		return self.lexeme

	# Can use this like Type.INT()
	# @classmethod
	# def INT(cls):
	# 	return cls("int", Tag.BASIC, 4)

# Initialize static class variables
Type.static_variables()
