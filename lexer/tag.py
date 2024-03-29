'''
Tag class to keep all the reserved words operators
'''
class Tag:
	IF = 259
	ELSE = 260
	WHILE = 261
	FOR = 262
	RETURN = 263
	PARANTHESIS_OPEN = 264
	PARANTHESIS_CLOSE = 265
	SQR_BRACKET_OPEN = 266
	SQR_BRACKET_CLOSE = 267
	CURLY_BRACKETS_OPEN = 268
	CURLY_BRACKETS_CLOSE = 269
	SEMICOLON = 270
	COLON = 271
	MULTIPLY = 272
	DIVIDE = 273
	PLUS = 274
	MINUS = 275
	ASSIGN = 276
	GT = 277
	LT = 278
	GE = 279
	LE = 280
	NE = 281
	EQ = 282
	PLUS_EQ = 283
	MINUS_EQ = 284
	AND = 285
	OR = 286
	NOT = 287
	NUM = 288
	HEX = 289
	REAL = 290
	ID = 291
	COMMA = 292
	BITWISE_AND = 293
	BITWISE_OR = 294
	BASIC = 295
	INDEX = 296
	TEMP = 297
	TRUE = 298
	FALSE = 299
	BREAK = 300
	DO = 301
	RETURN = 302
	

	INVERSE_DICT = {
		259: 'IF',
		260: 'ELSE',
		261: 'WHILE',
		262: 'FOR',
		263: 'RETURN',
		264: 'PARANTHESIS OPEN',
		265: 'PARANTHESIS CLOSE',
		266: 'SQUARE BRACKET OPEN',
		267: 'SQUARE BRACKET CLOSE',
		268: 'CURLY BRACKETS OPEN',
		269: 'CURLY BRACKETS CLOSE',
		270: 'SEMICOLON',
		271: 'COLON',
		272: 'MULTIPLY',
		273: 'DIVIDE',
		274: 'PLUS',
		275: 'MINUS',
		276: 'ASSIGN',
		277: 'GT',
		278: 'LT',
		279: 'GE',
		280: 'LE',
		281: 'NE',
		282: 'EQ',
		283: 'PLUS EQUAL',
		284: 'MINUS EQUAL',
		285: 'AND',
		286: 'OR',
		287: 'NOT',
		288: 'NUM',
		289: 'HEX',
		290: 'REAL',
		291: 'ID',
		292: 'COMMA',
		293: 'BITWISE AND',
		294: 'BITWISE OR',
		298: 'TRUE',
		299: 'FALSE',
		300: 'BREAK',
		301: 'DO',
		302: 'RETURN'
	} 

