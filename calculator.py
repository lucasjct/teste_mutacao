def soma(x,y):
    return x + y

def multiplicacao(x, y):
    return x * y

def comparador(val1, val2):
    if val1 > val2:
        return True
    else:
        return False

def iterador(x):
    results = 0
    for value in range(x):
        results = results + value
    return results

def par_impar(num):
    if num % 2 == 1:
        return "ímpar"
    else:
        return "par"
