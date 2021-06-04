from inter.expr import Expr
from lexer.token import Token
from symbols.type import Type


'''
Class for Identifiers
'''
class Id(Expr):
	def __init__(self, op: Token, p: Type, offset: int):
		super().__init__(op, p)
		# Offset is the relative address of identifier
		self.offset = offset

