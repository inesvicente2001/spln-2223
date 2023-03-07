import ply.lex as lex

literals = [';','\n','-',' ']

tokens = {'PALTRAD', 'LIN', 'TEMA'}

def t_PALTRAD(t): r'[\w ]+'

def t_LIN(t): r'ga|pt|en|es'

def t_TEMA(t): r'[\w ]+'