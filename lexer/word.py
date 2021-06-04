from lexer.tag import Tag
from lexer.token import Token


class Word(Token):

	@classmethod
	def static_variables(cls):
		cls._AND: Word = Word("&&", Tag.AND)
		cls._OR: Word =  Word("||", Tag.OR)
		cls._NOT: Word = Word("!", Tag.NOT)
		cls.BITWISE_AND = Word("&", Tag.BITWISE_AND)
		cls.BITWISE_OR = Word("|", Tag.BITWISE_OR)
		cls.ASSIGN: Word = Word("=", Tag.ASSIGN)
		cls.NE: Word = Word("!=", Tag.NE)
		cls.EQ: Word = Word("==", Tag.EQ)
		cls.LT: Word = Word("<", Tag.LT)
		cls.GT: Word = Word(">", Tag.GT)
		cls.LE: Word = Word("<=", Tag.LE)
		cls.GE: Word = Word(">=", Tag.GE)
		cls.PLUS_EQ: Word = Word("+=", Tag.PLUS_EQ)
		cls.MINUS_EQ: Word = Word("-=", Tag.MINUS_EQ)
		cls.SEMICOLON: Word = Word(";", Tag.SEMICOLON)
		cls.COLON: Word = Word(":", Tag.COLON)
		cls.COMMA: Word = Word(",", Tag.COMMA)
		cls.PLUS: Word = Word("+", Tag.PLUS)
		cls.MINUS: Word = Word("-", Tag.MINUS)
		cls.MULTIPLY: Word = Word("*", Tag.MULTIPLY)
		cls.DIVIDE: Word = Word("/", Tag.DIVIDE)
		cls.PARANTHESIS_OPEN: Word = Word("(", Tag.PARANTHESIS_OPEN)
		cls.PARANTHESIS_CLOSE: Word = Word(")", Tag.PARANTHESIS_CLOSE)
		cls.SQR_BRACKET_OPEN: Word = Word("[", Tag.SQR_BRACKET_OPEN)
		cls.SQR_BRACKET_CLOSE: Word = Word("]", Tag.SQR_BRACKET_CLOSE)
		cls.CURLY_BRACKETS_OPEN: Word = Word("{", Tag.CURLY_BRACKETS_OPEN)
		cls.CURLY_BRACKETS_CLOSE: Word = Word("}", Tag.CURLY_BRACKETS_CLOSE)
		cls.TEMP: Word = Word("temp", Tag.TEMP)
		cls.TRUE: Word = Word("true", Tag.TRUE)
		cls.FALSE: Word = Word("false", Tag.FALSE)

	def __init__(self, s: str, tag: int):
		super().__init__(tag)
		self.lexeme = s

	def printToken(self):
		super().printToken()
		print(self.lexeme, sep='')

	def to_string(self):
		return self.lexeme

# Initialize static variables
Word.static_variables()
