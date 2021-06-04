from lexer.token import Token
from inter.expr import Expr
from inter.temp import Temp
from symbols.type import Type

'''
Class for operators. This class implements reduce function
to calculate the value according to the operator.
'''
class Op(Expr):
	def __init__(self, op: Token, p: Type):
		super().__init__(op, p)

	def reduce(self) -> Temp:
		# Get right side of the expression
		expr: Expr = self.gen()

		# Calculate temporary representation of the right side
		t: Temp = Temp(self.type)
		
		self.emit(f'{t.to_string()} = {expr.to_string()}')

		return t
