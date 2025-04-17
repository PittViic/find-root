# Criar um programa que encontre as raizes das equações transcendentes por aproximação 

"""
OBS: 
        1. Ter que aceitar novos intervalos e novos erros
        2. Tem que apresentar a tabela do intervalo procurado e o tesste da raiz
        3. O método de busca por bisseção de intervalos
    
O programa tem que resolver as seguintes equações com o erro dado:
    a) ln x - 10 = 0; [0, 7] - E < 10^-5

    b) arctan(x) + x² - 4 = 0; [-6, 4] - E < 10^-5
"""

""" 
DEFINIÇÃO: Seja f uma função contínua em um intervalo fechado [a, b] e N um número qualquer entre f(a) e f(b), sendo f(a) != f(b). Então existe um número c no intervalo (a, b) tal que f(c) = N.
"""

# As funções polinomiais, racionais, trigonométricas, exponenciais e logarítmicas, são contínuas em todos os pontos de seus domínios.

# Developed by Pedro Victor - 
# @pe_viic

import math
import sympy as sp

x = sp.symbols('x')
expressao1 = sp.ln(x) - 10
expressao2 = sp.atan(x) + x**2 - 4

def verify_continuity(expr, variavel, intervalo=None):
    expr = sp.simplify(expr)
    
    descontinuidades = sp.singularities(expr, variavel)
    
    if intervalo:
        descontinuidade_intervalo = [p for p in descontinuidades if p.is_real and intervalo[0] <= p <= intervalo[1]]
        if descontinuidade_intervalo:
            print(f"A expressao não é continua nos pontos: {descontinuidade_intervalo}")
            return False
        else:
            print(f"A expressão é contínua no intervalo: {intervalo}")
            return True

def letraA(x):
    return math.log(x) - 10

def letraB(x):
    return math.atan(x) + math.pow(x, 2) - 4

def rootA(intervalA, intervalB, erro):
    while(True):
        if(res1 * res2 > 0):
            res1 = letraA(intervalA)
            res2 = letraA(intervalB)
        else:
            return
        
def main():
    print("1 - Questão 1\n2 - Questão 2")
    question = input("Selecione: ")
    
    if question == 1:
        # Questão 1
        intervalo1 = input("Valor do intervalo: ")
        intervalo2 = input("Valor do intervalo: ")
        erro = input("Valor do erro: ")
        
        verify_continuity(expressao1, x, [intervalo1, intervalo2])
        
        if verify_continuity == True:
            rootA()
    else:
        # Questão 2
        intervalo1 = input("Valor do intervalo: ")
        intervalo2 = input("Valor do intervalo: ")
        erro = input("Valor do erro: ")
        
        verify_continuity(expressao1, x, [intervalo1, intervalo2])
        
        if verify_continuity == True:
            