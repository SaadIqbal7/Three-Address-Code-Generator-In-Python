from lexer._lexer import Lexer

'''
Node class for each node in the syntax tree
'''
class Node:
	labels = 0

	def __init__(self):
		# Line number that each node keeps
		self.lexline = Lexer.line

	# As errors are checked in the syntax tree, each node has represents its own error
	def error(self, s: str):
		raise Exception(f'near line {self.lexline}: {s}')

	def new_label(self) -> int:
		Node.labels += 1
		return Node.labels

	def emit_label(self, i: int):
		print(f'L{i}:', end='')
	
	def emit(self, s: str):
		print(f'\t{s}')
