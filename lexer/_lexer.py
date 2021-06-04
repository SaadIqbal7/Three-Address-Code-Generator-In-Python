from lexer.hex import Hex
from lexer.num import Num
from lexer.real import Real
from lexer.tag import Tag
from lexer.token import Token
from lexer.word import Word
from symbols.type import Type


class Lexer:
	# Define line for line number
	line = 1

	def __init__(self, filename: str):
		# Buffer to store all characters
		self.buffer = []

		# Open file passed to the constructor
		with open(filename, mode='r') as fd:
			# Read file into buffer
			while True:
				char = fd.read(1)
				if char == '':
					break
				self.buffer.append(char)

		# A dictionary for reserve words and identifiers
		self.words = {}

		self.reserve(Word("if", Tag.IF))
		self.reserve(Word("else", Tag.ELSE))
		self.reserve(Word("while", Tag.WHILE))
		self.reserve(Word("do", Tag.DO))
		self.reserve(Word("break", Tag.BREAK))
		self.reserve(Word("return", Tag.RETURN))
		
		self.reserve(Word.TRUE)
		self.reserve(Word.FALSE)
		self.reserve(Type.INT)
		self.reserve(Type.FLOAT)
		self.reserve(Type.CHAR)
		self.reserve(Type.BOOL)

		# A pointer to read each character
		self.peek = ' '

		# Pointer to character in buffer
		self.currentChar = 0

	# Store reserved words in words dictionary
	def reserve(self, word: Word):
		self.words[word.lexeme] = word

	# Read single character from file
	def readch(self):
		# Read character and store it in peek
		self.peek = self.buffer[self.currentChar]
		self.currentChar += 1

	# Reads character from file and checks if the character
	# read matches with the passed character
	def read_specific_ch(self, char: str) -> bool:
		# Read character
		self.readch()

		# Check if characters match
		if(self.peek != char):
			return False

		# Reset peek, means we want to proceed to next characters
		# or the characters in file have ended
		self.peek = ' '

		return True

	# Retract one step back in buffer
	def retract(self):
		self.currentChar -= 1
	
	def getNextToken(self):
		while True:
			# Read charater from file
			self.readch()

			# Check if all the file is read
			if self.currentChar >= len(self.buffer):
				return None
			# Check if character is empty space or tab character
			if self.peek == ' ' or self.peek == '\t':
				continue
			# Check if new line is encurrentChars
			elif self.peek == '\n':
				# Change line
				Lexer.line += 1
			else:
				break

	def scan(self) -> Token:
		self.getNextToken()

		# Check for comment
		if self.comment():
			# Move on reading
			self.getNextToken()

		# Check for operators
		op = self.operator()

		if op != None:
			return op

		# Check for number
		num = self.number()
		
		if num != None:
			self.retract()
			return num

		# Check for word
		word = self.word()

		if word != None:
			self.retract()
			return word

		# Add case for array
		
		self.peek = ' '
		# Else return error
		return None

	def operator(self) -> Token:
		if self.peek == '(':
			return Word.PARANTHESIS_OPEN
		elif self.peek == ')':
			return Word.PARANTHESIS_CLOSE
		elif self.peek == '[':
			return Word.SQR_BRACKET_OPEN
		elif self.peek == ']':
			return Word.SQR_BRACKET_CLOSE
		elif self.peek == '{':
			return Word.CURLY_BRACKETS_OPEN
		elif self.peek == '}':
			return Word.CURLY_BRACKETS_CLOSE
		elif self.peek == ';':
			return Word.SEMICOLON
		elif self.peek == ':':
			return Word.COLON
		elif self.peek == ',':
			return Word.COMMA
		elif self.peek == '*':
			return Word.MULTIPLY
		elif self.peek == '/':
			return Word.DIVIDE
		elif self.peek == '+':
			if self.read_specific_ch('='):
				return Word.PLUS_EQ
			else:
				self.retract()
				return Word.PLUS
		elif self.peek == '-':
			if self.read_specific_ch('='):
				return Word.MINUS_EQ
			else:
				self.retract()
				return Word.MINUS
		elif self.peek == '<':
			if self.read_specific_ch('='):
				return Word.LE
			else:
				self.retract()
				return Word.LT
		elif self.peek == '>':
			if self.read_specific_ch('='):
				return Word.GE
			else:
				self.retract()
				return Word.GT
		elif self.peek == '=':
			if self.read_specific_ch('='):
				return Word.EQ
			else:
				self.retract()
				return Word.ASSIGN
		elif self.peek == '!':
			if self.read_specific_ch('='):
				return Word.NE
			else:
				self.retract()
				return Word._NOT
		elif self.peek == '&':
			if self.read_specific_ch('&'):
				return Word._AND
			else:
				self.retract()
				return Word.BITWISE_AND
		elif self.peek == '|':
			if self.read_specific_ch('|'):
				return Word._OR
			else:
				self.retract()
				return Word.BITWISE_OR

		return None

	# Checks for number and hex number
	def number(self) -> Token:
		# Check if number is a hex number
		_hex = self._hex()

		if _hex != None:
			return _hex

		# Check if character is number
		if self.peek.isdigit():
			num = 0

			# Check if character is number
			while self.peek.isdigit():
				# Determine number
				num = num * 10 + int(self.peek)
				# Read next character
				self.readch()

			# Check if a point "." is not encurrentChared
			if self.peek != '.':
				return Num(num)
			else:
				d = 10.0
				while True:
					# Read next character
					self.readch()
					if not self.peek.isdigit():
						break

					# Determine number
					num = num + int(self.peek) / d
					d = d * 10
				
				return Real(num)
		else:
			return None

	# Checks for hex number
	def _hex(self):
		# Check if character is a digit
		if self.peek.isdigit():
			# Check if character is 0
			if self.peek == '0':
				# Read next character
				self.readch()

				# Check if read character is an 'x'
				if self.peek == 'x':
					hex_digit = ['0x']
					while True:
						# Read next digit
						self.readch()

						unicode_rep = ord(self.peek)
						# Check if character is a hex digit
						if (unicode_rep >= 48 and unicode_rep <= 57) \
							or  (unicode_rep >= 65 and unicode_rep <= 70):
							hex_digit.append(self.peek)
						else:
							return Hex(''.join(hex_digit))
				else:
					# Go back to '0'
					self.retract()
					self.retract()
					# Read zero
					self.readch()
		return None
	
	# Check for a identifier or a reserved word
	def word(self) -> Token:
		# Check if character read is an alphabet
		if self.peek.isalpha():
			word = []
			# Read characters until there is an alphabet or number
			while self.peek.isalnum():
				word.append(self.peek)
				# Read next character
				self.readch()

			word = ''.join(word)

			# Check if read word is a keyword
			if word in self.words:
				return self.words[word]
			else:
				# Else it is an identifier and will most likely appear again
				# in the program
				self.words[word] = Word(word, Tag.ID)

				return self.words[word]
		return None

	# Checks for comments and returns true if comment is found
	def comment(self) -> bool:
		# Check if character is a comment
		if self.peek == '/':
			# Check if next character is a start
			self.readch()
			if self.peek == '*':
				# Read characters until next * is not found
				while True:
					self.readch()

					if self.peek == '*':
						# Check if next character is /
						self.readch()

						if self.peek == '/':
							return True
						else:
							self.retract()
			else:
				self.retract()

		return False		

	def printToken(self, token: Token):
		print("Line Number:", line)
		token.printToken()

