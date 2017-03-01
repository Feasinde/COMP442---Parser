class NonTerminal:
	"""NonTerminal class"""
	__symbol = ''
	def __init__(self, first_set, follow_set, symbol, production):
		self._symbol = symbol
		self._first = first_set
		self._follow = follow_set
		self._production = production