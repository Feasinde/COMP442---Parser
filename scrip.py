terminals = ['id','class','{','}','(',')','if','else','get',
			 'for','return','put','EPSILON', '==','!=','<>','>=','<=',
			 'and','or']
with open('transformed_grammar_bnf.txt', 'w') as output:
	with open('transformed_grammar_NLA.txt') as file:
		for line in file:
			list_line = line.split()
			for token in list_line:
				if token == '->': token = '::='
				elif token != '\n' and len(token) > 1 and token not in terminals: token = '<'+token+'>'
				output.write(token+' ')
			output.write('\n')
with open('transformed_grammar_LaTeX.txt', 'w') as output:
	with open('transformed_grammar_bnf.txt') as file:
		for line in file:
			for token in line.split():
				if token == '::=': token = ' & '+token+' & '
				if token == '{' or token == '}' or token == '_' : token = '\\' + token
				output.write(token)
			output.write(' \\\\ \n')