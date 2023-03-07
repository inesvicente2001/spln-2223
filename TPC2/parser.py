import ply.yacc as yacc

def p_1(p): "dic: LPAL" ; pass

def p_2(p): "LPAL: PAL '\n' '\n' LPAL" ; pass

def p_3(p): "LPAL: PAL" ; pass

def p_4(p): "PAL: LTEMA '\n' LTRAD" ; pass

def p_5(p): "LTEMA: TEMA ';' ' ' LTEMA" ; pass

def p_6(p): "LTEMA: TEMA" ; pass

def p_7(p): "LTRAD: TRAD '\n' LTRAD" ; pass

def p_8(p): "LTRAD: TRAD" ; pass

def p_9(p): "TRAD: LIN ' ' '-' ' ' PALTRAD" ; pass

def p_10(p): "LPALTRAD: PALTRAD ';' ' ' LPALTRAD" ; pass

def p_11(p): "LPALTRAD: PALTRAD" ; pass