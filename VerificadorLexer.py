import sys
import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = (t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    sys.exit(1)

lex.lex() # Build the lexer

def verificarCadena(cadena):
	listaCaracteres = []
	lex.input(cadena)
	while True:
	    tok = lex.token()
	    if tok != None:
	    	listaCaracteres.append(tok.value)
	    if not tok:
	    	break
	    print str(tok.value) + " - " + str(tok.type)
	return listaCaracteres