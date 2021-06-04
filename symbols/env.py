from lexer.token import Token
from inter.id import Id

class Env:
	def __init__(self, n):
		self.table = {}
		self.prev: Env = n

	# Function to put word and its id in the table
	def put(self, w: Token, _id: Id):
		self.table[w] = _id

	# Function to get id for the word
	def get(self, w: Token) -> Id:
		e:Env = self
		while True:
			_id: Id = e.table.get(w, None)

			if _id:
				return _id
			
			e = e.prev

			if e == None:
				break

		return None




