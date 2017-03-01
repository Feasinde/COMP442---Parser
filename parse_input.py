from NonTerminal import NonTerminal
from Parser import Parser
from LexicalAnalyser import Lexer
import argparse

            ################################################
            ####### Begin parse table implementation #######
            ################################################

## Implement the grammar as a list of NonTerminal objects

rulz = []
rulz.append(NonTerminal({'class', 'program'}, {}, 'prog', ['N1', 'progBody']))
rulz.append(NonTerminal({'class'}, {}, 'classDecl', ['class', 'id', '{', 'A1', '}', ';']))
rulz.append(NonTerminal({'program'},{}, 'progBody', ['program', 'funcBody', ';', 'N3']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'funcHead', ['type', 'id', '(', 'fParams', ')']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'funcDef', ['funcHead', 'funcBody']))
rulz.append(NonTerminal({'{'}, {}, 'funcBody', ['{', 'A4', '}']))
rulz.append(NonTerminal({'id'}, {}, 'statement', ['assignStat', ';']))
rulz.append(NonTerminal({'return'}, {}, 'statement',['return', '(', 'expr', ')', ';']))
rulz.append(NonTerminal({'put'}, {}, 'statement',['put', '(', 'expr', ')', ';']))
rulz.append(NonTerminal({'get'}, {}, 'statement',['get', '(', 'variable', ')', ';']))
rulz.append(NonTerminal({'if'}, {}, 'statement',['if', '(', 'expr', ')', 'then', 'statBlock', 'else', 'statBlock', ';']))
rulz.append(NonTerminal({'for'}, {}, 'statement',['for', '(', 'type', 'id', 'assignOp', 'expr', ';', 'relExpr', ';', 'assignStat', ')', 'statBlock', ';']))
rulz.append(NonTerminal({'id'}, {}, 'assignStat',['variable', 'assignOp', 'expr']))
rulz.append(NonTerminal({'EPSILON'}, {';', 'else'}, 'statBlock', ['EPSILON']))
rulz.append(NonTerminal({'for', 'if', 'get', 'put', 'return', 'id'}, {}, 'statBlock', ['statement']))
rulz.append(NonTerminal({'{'}, {}, 'statBlock',['{', 'N4', '}']))
rulz.append(NonTerminal({'(', 'not', 'id', 'float_num', 'integer', '+', '-'}, {}, 'expr',['arithExpr', 'L1']))
rulz.append(NonTerminal({'(', 'num', 'not', 'id', '+', '-'}, {}, 'relExpr',['arithExpr', 'relOp', 'arithExpr']))
rulz.append(NonTerminal({'(', 'not', 'id', 'float_num', 'integer', '+', '-'}, {}, 'arithExpr',['term', 'L2']))
rulz.append(NonTerminal({'+'}, {}, 'sign', ['+']))
rulz.append(NonTerminal({'-'}, {}, 'sign',['-']))
rulz.append(NonTerminal({'(', 'not', 'id', 'float_num', 'integer', '+', '-'}, {}, 'term',['factor', 'L3']))
rulz.append(NonTerminal({'+', '-'}, {}, 'factor',['sign', 'factor']))
rulz.append(NonTerminal({'id'}, {}, 'factor', ['A8', 'L4']))
rulz.append(NonTerminal({'not'}, {}, 'factor', ['not', 'factor']))
rulz.append(NonTerminal({'float_num', 'integer'}, {}, 'factor', ['num']))
rulz.append(NonTerminal({'('}, {}, 'factor',['(', 'arithExpr', ')']))
rulz.append(NonTerminal({'id'}, {}, 'variable', ['A8']))
rulz.append(NonTerminal({'['}, {}, 'indice', ['[', 'arithExpr', ']']))
rulz.append(NonTerminal({'['}, {}, 'arraySize',['[', 'integer', ']']))
rulz.append(NonTerminal({'int'}, {}, 'type', ['int']))
rulz.append(NonTerminal({'id'}, {}, 'type', ['id']))
rulz.append(NonTerminal({'float'}, {}, 'type', ['float']))
rulz.append(NonTerminal({'EPSILON'}, {')'}, 'fParams', ['EPSILON']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'fParams', ['type', 'id', 'N5', 'N8']))
rulz.append(NonTerminal({'EPSILON'}, {')'}, 'aParams', ['EPSILON']))
rulz.append(NonTerminal({'(', 'num', 'not', 'id', '+', '-'}, {}, 'aParams', ['expr', 'N9']))
rulz.append(NonTerminal({','}, {}, 'fParamsTail', ['type', 'id', 'N5']))
rulz.append(NonTerminal({','}, {}, 'aParamsTail',['expr']))
rulz.append(NonTerminal({'='}, {}, 'assignOp', ['=']))
rulz.append(NonTerminal({'>='}, {}, 'relOp',['>=']))
rulz.append(NonTerminal({'>'}, {}, 'relOp',['>']))
rulz.append(NonTerminal({'=='}, {}, 'relOp',['==']))
rulz.append(NonTerminal({'<>'}, {}, 'relOp',['<>']))
rulz.append(NonTerminal({'<='}, {}, 'relOp',['<=']))
rulz.append(NonTerminal({'<'}, {}, 'relOp',['<']))
rulz.append(NonTerminal({'or'}, {}, 'addOp',['or']))
rulz.append(NonTerminal({'-'}, {}, 'addOp',['-']))
rulz.append(NonTerminal({'+'}, {}, 'addOp',['+']))
rulz.append(NonTerminal({'and'}, {}, 'multOp',['and']))
rulz.append(NonTerminal({'/'}, {}, 'multOp',['/']))
rulz.append(NonTerminal({'*'}, {}, 'multOp',['*']))
rulz.append(NonTerminal({'EPSILON'}, {'program'}, 'N1',['EPSILON']))
rulz.append(NonTerminal({'class'}, {}, 'N1',['classDecl', 'N1']))
rulz.append(NonTerminal({'EPSILON'}, {'$'}, 'N3',['EPSILON']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'N3',['funcDef', ';', 'N3']))
rulz.append(NonTerminal({'EPSILON'}, {'}'}, 'N4',['EPSILON']))
rulz.append(NonTerminal({'for', 'if', 'get', 'put', 'return', 'id'}, {}, 'N4',['statement', 'N4']))
rulz.append(NonTerminal({'EPSILON'}, {';', ',', '}', 'float', 'id', 'int', 'for', 'if', 'get', 'put', 'return', ')'}, 'N5',['EPSILON']))
rulz.append(NonTerminal({'['}, {}, 'N5',['arraySize', 'N5']))
rulz.append(NonTerminal({'EPSILON'}, {'.', ';', ')', ',', '<', '<=', '<>', '==', '>', '>=', ']', '+', '-', 'or', '*', '/', 'and', '(', '='}, 'N7',['EPSILON']))
rulz.append(NonTerminal({'['}, {}, 'N7',['indice', 'N7']))
rulz.append(NonTerminal({'EPSILON'}, {')'}, 'N8',['EPSILON']))
rulz.append(NonTerminal({','}, {}, 'N8',['fParamsTail', 'N8']))
rulz.append(NonTerminal({'EPSILON'}, {')'}, 'N9',['EPSILON']))
rulz.append(NonTerminal({','}, {}, 'N9',['aParamsTail', 'N9']))
rulz.append(NonTerminal({'EPSILON'}, {';', ')', ',', '}', 'id', 'for', 'if', 'get', 'put', 'return', 'float', 'int'}, 'L1', ['EPSILON']))
rulz.append(NonTerminal({'<', '<=', '<>', '==', '>', '>='}, {}, 'L1',['relOp', 'arithExpr']))
rulz.append(NonTerminal({'EPSILON'}, {';', ')', ',', '}', 'id', 'for', 'if', 'get', 'put', 'return', 'float', 'int', '<', '<=', '<>', '==', '>', '>=', ']'}, 'L2', ['EPSILON']))
rulz.append(NonTerminal({'+', '-', 'or'}, {}, 'L2', ['addOp', 'term', 'L2']))
rulz.append(NonTerminal({'EPSILON'}, {';', ')', ',', '}', 'id', 'for', 'if', 'get', 'put', 'return', 'float', 'int', '<', '<=', '<>', '==', '>', '>=', ']', '+', '-', 'or'}, 'L3', ['EPSILON']))
rulz.append(NonTerminal({'*','/', 'and'}, {}, 'L3', ['multOp', 'factor', 'L3']))
rulz.append(NonTerminal({'EPSILON'}, {';', ')', ',', '}', 'id', 'for', 'if', 'get', 'put', 'return', 'float', 'int', '<', '<=', '<>', '==', '>', '>=', ']', '+', '-', 'or', '*', '/', 'and'}, 'L4', ['EPSILON']))
rulz.append(NonTerminal({'('}, {}, 'L4', ['(', 'aParams', ')']))
rulz.append(NonTerminal({'EPSILON'}, {'}'}, 'A1', ['EPSILON']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'A1', ['A2', 'A1']))
rulz.append(NonTerminal({'float', 'id', 'int'}, {}, 'A2',['type', 'id', 'A3']))
rulz.append(NonTerminal({'[', ';'}, {';'}, 'A3', ['N5', ';']))
rulz.append(NonTerminal({'('}, {}, 'A3', ['(', 'fParams', ')', 'funcBody', ';']))
rulz.append(NonTerminal({'EPSILON'}, {'}'}, 'A4', ['EPSILON']))
rulz.append(NonTerminal({'id', 'for', 'if', 'get', 'put', 'return', 'float', 'int'}, {}, 'A4', ['A5', 'A4']))
rulz.append(NonTerminal({'for', 'if', 'get', 'put', 'return', 'float', 'int'}, {}, 'A5', ['A7']))
rulz.append(NonTerminal({'id'}, {}, 'A5',['id', 'A6']))
rulz.append(NonTerminal({'.', '[', '='}, {}, 'A6', ['N7', 'A9', 'assignOp', 'expr', ';']))
rulz.append(NonTerminal({'id'}, {}, 'A6',['id', 'N5', ';']))
rulz.append(NonTerminal({'id'}, {}, 'A8', ['id', 'N7', 'A9']))
rulz.append(NonTerminal({'EPSILON'}, {'=', ';', ')', ',', '<', '<=', '<>', '==', '>', '>=', ']', '+', '-', 'or', '*', '/', 'and', '('}, 'A9',['EPSILON']))
rulz.append(NonTerminal({'.'}, {}, 'A9', ['.', 'A8']))
rulz.append(NonTerminal({'float', 'int'}, {}, 'A7',['A10', 'id', 'N5', ';']))
rulz.append(NonTerminal({'return'}, {}, 'A7', ['return', '(', 'expr', ')', ';']))
rulz.append(NonTerminal({'put'}, {}, 'A7', ['put', '(', 'expr', ')', ';']))
rulz.append(NonTerminal({'get'}, {}, 'A7', ['get', '(', 'variable', ')', ';']))
rulz.append(NonTerminal({'if'}, {}, 'A7', ['if', '(', 'expr', ')', 'then', 'statBlock', 'else', 'statBlock', ';']))
rulz.append(NonTerminal({'for'}, {}, 'A7', ['for', '(', 'type', 'id', 'assignOp', 'expr', ';', 'relExpr', ';', 'assignStat', ')', 'statBlock', ';']))
rulz.append(NonTerminal({'int'}, {}, 'A10', ['int']))
rulz.append(NonTerminal({'float'}, {}, 'A10', ['float']))
rulz.append(NonTerminal({'integer'}, {}, 'num', ['integer']))
rulz.append(NonTerminal({'float_num'}, {}, 'num', ['float_num']))

## Build list of terminals
terminals = [
'class',
'id',
'{','}',
'.',
',',
';',
'program',
'id',
'(',')',
'if','then','else',
'for',
'get',
'put',
'return',
'+','-',
'not',
'[',']',
'integer','int','float', 'float_num',
'=','==','<>','<','>','<=','>=',
'and','or',
'*','/'
]

## Build dictionary of dictionaries that represents the parse table
parse_table = {}
for rule in rulz:
	parse_table[rule._symbol] = {}


## Fill the table according to slide 4-18
for rule in rulz:
	for t in terminals:
		if t in rule._first:
			parse_table[rule._symbol][t] = rule
		if 'EPSILON' in rule._first:
			for t2 in terminals:
				if t2 in rule._follow:
					parse_table[rule._symbol][t2] = rule

with open('code_sample_from_assignment.txt') as file:
	input_string = file.read()


parser = Parser()
parser._setInput(input_string)
parser._parse(rulz, terminals, parse_table, print_stack=True)

            ###############################################
            ####### End parse table implementation ########
            ###############################################
                                 ###
                                 ###
                                 ###
                               #######
                                #####
                                 ###
                                  # 
            ###############################################
            #### Begin command line call implementation ###
            ###############################################

# Setup flags and parameters
# arg_parser = argparse.ArgumentParser(prog='Parser', description='Takes a source file and parses it for syntax errors')
# arg_parser.add_argument('-f', '--file')
# arg_parser.add_argument('-s', '--stack', action='store_true')
# arg_parser.add_argument('-d', '--derivation', action='store_true')
# args = arg_parser.parse_args()

# if args.stack:
# 	print_stack = True
# else: print_stack = False

# if args.derivation:
#     print_derivation = True
# else: print_derivation = False

# with open(args.file) as file:
# 	input_string = file.read()

# parser = Parser()
# parser._setInput(input_string)
# parser._parse(rulz, terminals, parse_table, print_stack, print_derivation)