from lexer._lexer import Lexer
from _parser.parser import Parser
import sys


def main(filename):
	# Make lexical analyser instance
	lex: Lexer = Lexer(filename)
	parse: Parser = Parser(lex)
	parse.program()
	print()

if __name__ == '__main__':
	if len(sys.argv) == 1:
		# Read from user
		filename = input('Enter filename: ')
	else:
		# Get filename
		filename = sys.argv[1]

	main(filename)



