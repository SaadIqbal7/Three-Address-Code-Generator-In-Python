from inter.op import Op
from lexer.token import Token
from inter.expr import Expr
from symbols.type import Type

'''
Class to evaluate arithematic operations
'''
class Arith(Op):
	def __init__(self, op: Token, expr1: Expr, expr2: Expr):
		super().__init__(op, None)
		self.expr1 = expr1
		self.expr2 = expr2
		# Find type by using max function
		self.type = Type.max(self.expr1.type, self.expr2.type)
		if self.type == None:
			self.error('type error')

	def gen(self):
		return Arith(self.op, self.expr1.reduce(), self.expr2.reduce())

	def to_string(self):
		return f'{self.expr1.to_string()} {self.op.to_string()} {self.expr2.to_string()}'

