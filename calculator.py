from numbers import Number

def soma(x,y):
    """AOR."""
    return x + y


def invert(x):
    """AOD - DELETE OPERATOR
       AOR - MUDA OPERATOR"""
    return -x


def sum_(*vals):
    """
    ASR - Troca o operador de atribuicao
    CRP - Troca as constantes
    """
    results = 0
    for val in vals:
        results += val
    return results


def is_number(val):
    """ 
    COD - Deletar operadores sozinho (not)
    COI - Insere um operador lógico
    """
    if not isinstance(val, Number):
        return False
    return True

def check_number(x,y):
    if is_number(x) and is_number(y):
        return True
