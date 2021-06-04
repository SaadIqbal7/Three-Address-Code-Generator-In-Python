from inter.expr import Expr
from lexer.token import Token
from symbols.type import Type
from lexer.num import Num
from lexer.tag import Tag
from lexer.word import Word


"""
A constant class which acts as a leaf in syntax tree.
A constant can be a constant integer, character etc.
It takes a token and a type to represent tht constant
"""
class Constant(Expr):

	@classmethod
	def static_variables(cls):
		cls.TRUE = Constant(Word.TRUE, Type.BOOL)
		cls.FALSE = Constant(Word.FALSE, Type.BOOL)

	def __init__(self, token: Token=None, p: Type=None, value: int=None):
		# Default constructor
		if token != None and p != None:
			super().__init__(token, p)
		# Make a constant  integar object
		elif value != None:
			super().__init__(Num(value), Type.INT)

	# Jumping to t or f
	# t represent code to be executed when Constant is True
	# f represent code to be executed when Constant is False
	# t = True
	# f = False
	def jumping(self, t: int, f: int):
		if self == Constant.TRUE and t != 0:
			self.emit(f'goto L{t}')
		elif self == Constant.FALSE and f != 0:
			self.emit(f'goto L{f}')


# Initialize static variables
Constant.static_variables()

