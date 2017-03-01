from LexicalAnalyser import Lexer

class Parser:
	def __init__(self):
		self._stack = ['$']

	def _push(self, t):
		self._stack.append(t)

	def _pop(self):
		self._stack.pop()

	def _top(self):
		return self._stack[-1]

	def _setInput(self, input_string):
		self._input = input_string

	def _inverse_RHS_multiple_push(self, rule):
		length_of_production = len(rule._production)
		for i in range(length_of_production):
			self._push(rule._production[-i-1])
	
	def _parse(self, rulz, terminals, parse_table, print_stack=False, print_derivation=False):
		## Initialise lexer
		tokeniser = Lexer(self._input)

		## Initialise derivation
		current_derivation = [rulz[0]._symbol]

		## Push S into the parser stack
		self._push(rulz[0]._symbol)
		rule_x = rulz[0]

		## Define derivation method
		def derivation(current_derivation):
			first_nonterminal = 0
			t = current_derivation[first_nonterminal]
			while t not in terminals and first_nonterminal < len(current_derivation):
				t = current_derivation[first_nonterminal]
				first_nonterminal += 1
			return_derivation = current_derivation[0:first_nonterminal]
			production = rule_x._production
			return_derivation = return_derivation + production + current_derivation[first_nonterminal+1:]
			return return_derivation
		
		## Define skipError function
		def skipError(line_number,a):
			print('Syntax error at line',line_number)
			if a == '$' or a in rule_x._follow:
				self._pop()
			else:
				while (a not in rule_x._first or ('EPSILON' in rule_x._first and a not in rule_x._follow)) and token != None:
					token = tokeniser.nextToken()
					a = token[0]
					print(token)
			print('leaving skiperror')

		## Define nextToken method so that no white space
		## is returned
		def nextToken():
			token = tokeniser.nextToken()
			a = token[0]
			while a == 'WHITE_SPACE':
				token = tokeniser.nextToken()
				a = token[0]
			return token

		## Begin parsing section
		token = nextToken()
		a = token[0]
		error = False
		while self._top() != '$':
			x = self._top()
			if x in terminals:
				if x == a:
					self._pop()
					try:
						token = nextToken()
						a = token[0]
						line_number = token[2]
					except TypeError:
						a = '$'
				else: 
					error = True
					skipError(line_number,a)
			elif x == 'EPSILON':
				self._pop()
			else:
				self._pop()
				if a != '$':
					try:
						rule_x = parse_table[x][a]
						current_derivation = derivation(current_derivation)
						self._inverse_RHS_multiple_push(parse_table[x][a])
					except KeyError:
						error = True
						skipError(line_number,a)
				if print_stack != False: print('stack = ',self._stack)
				if print_derivation != False: print('derivation = ',' '.join(current_derivation))
		if error != True: 
			print('EVERYTHING IS AWESOME')
		else: print('Some errors were found.')
