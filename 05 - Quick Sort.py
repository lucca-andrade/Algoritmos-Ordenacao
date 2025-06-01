# Quick Sort

# USANDO PRIMEIRO OU ÚLTIMO ELEMENTO
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]  # Primeiro elemento como pivô
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    
    # pivo = lista[-1]  # Último elemento como pivô
    # menores = [x for x in lista[:-1] if x <= pivo]
    # maiores = [x for x in lista[:-1] if x > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)
    
lista = [10, 7, 8, 9, 1, 5]
print("Lista Ordenada (Primeiro Elemento):", quick_sort(lista))
# print("Lista Ordenada (Último Elemento):", quick_sort(lista))

'''
# USANDO ELEMENTO CENTRAL
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Caso base: lista com 0 ou 1 elementos já está ordenada

    pivo = lista[len(lista) // 2]  # Escolhendo o pivô (elemento central)
    esquerda = [x for x in lista if x < pivo]  # Elementos menores que o pivô
    meio = [x for x in lista if x == pivo]  # Elementos iguais ao pivô
    direita = [x for x in lista if x > pivo]  # Elementos maiores que o pivô

    return quick_sort(esquerda) + meio + quick_sort(direita)  # Conectando os resultados recursivamente

lista = [8, 3, 7, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort(lista)
print("Lista ordenada (Elemento Central):", lista_ordenada)
'''
'''
# USANDO PIVÔ ALEATÓRIO
import random

def quick_sort_aleatorio(lista):
    if len(lista) <= 1:
        return lista

    pivo = random.choice(lista)  # Escolhe um pivô aleatório

    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    return quick_sort_aleatorio(esquerda) + meio + quick_sort_aleatorio(direita)

lista = [8, 3, 7, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort_aleatorio(lista)
print("Lista ordenada (Pivô Aleatório):", lista_ordenada)
'''
'''
# USANDO MEDIANA DE 3
import random

def quick_sort_mediana(lista):
    if len(lista) <= 1:
        return lista

    # Mediana de três: primeiro, meio e último elemento
    primeiro = lista[0]
    meio = lista[len(lista) // 2]
    ultimo = lista[-1]
    pivo = sorted([primeiro, meio, ultimo])[1]  # Escolhe a mediana

    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    return quick_sort_mediana(esquerda) + meio + quick_sort_mediana(direita)


lista = [8, 3, 7, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort_mediana(lista)
print("Lista ordenada (Mediana de Três):", lista_ordenada)
'''
'''
# USANDO MEDIANA REAL
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = sorted(lista)[len(lista) // 2]  # Mediana real
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# Exemplo de uso
lista = [10, 7, 8, 9, 1, 5]
print("Lista Ordenada (Mediana Real):", quick_sort(lista))
'''


## VANTAGENS
# Tem uma boa performance em listas grandes, principalmente quando a recursão é otimizada.

# Não precisa de memória extra significativa, pois organiza os elementos diretamente na lista.

# Pode ser usado amplamente em muitas linguagens de programação e frameworks devido 
# à sua eficiência e simplicidade.

# Adapta-se bem a estruturas complexas e pode ser modificado para funcionar em diversas 
# estruturas de dados, como listas ligadas.


## DESVANTAGENS
# Se o pivô escolhido é muito ruim (por exemplo, o menor ou maior elemento em uma lista ordenada), 
# o tempo de execução pode chegar aumentar consideravelmente.

# Se o algoritmo não estiver otimizado, ele pode precisar de um grande consumo de memória 
# e chamadas recursivas excessivas.

# Pode ser instável, já que não garante que elementos iguais mantenham sua 
# ordem relativa original após a ordenação.

# Menos eficiente em listas pequenas. É recomendado usar outros algoritmos como Insertion Sort.

















