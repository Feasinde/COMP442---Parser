from LexicalAnalyser import Lexer

with open('code_sample_from_assignment.txt') as file:
	input_string = file.read()

tokeniser = Lexer(input_string)

def nextToken():
	a = tokeniser.nextToken()[0]
	while a == 'WHITE_SPACE':
		a = tokeniser.nextToken()[0]
	return a

for i in range(100):
	a = nextToken()
	print(a)