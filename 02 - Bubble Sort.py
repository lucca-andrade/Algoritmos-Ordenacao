# Bubble Sort

def bubble_sort(lista):
    numero_elementos = len(lista)
    for i in range(numero_elementos - 1):
        for j in range(numero_elementos - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista 

lista = [5, 1, 9, 3] 
lista_ordenada = bubble_sort(lista) 
print("Lista ordenada:", lista_ordenada)

'''
# VERSÃO OTIMIZADA
def bubble_sort(lista):
    numero_elementos = len(lista)
    for i in range(numero_elementos - 1):
        trocou = False
        for j in range(numero_elementos - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break  
    return lista

lista = [5, 1, 9, 3] 
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)
'''


## VANTAGENS
# Fácil de entender e implementar.

# O algoritimo é estável e mantém a ordem relativa de elementos iguais.

# Pode ser otimizado, de forma que o algoritmo interrompa o loop se a lista já estiver ordenada 
# antes do fim das iterações.

# Funciona bem para listas pequenas.


## DESVANTAGENS
# Sempre percorre a lista inteira, realizando muitas comparações desnecessárias.

# Tempo de execução maior devido a grande quantidade de trocas realizadas.

# Ineficiente com listas grandes.

# Desempenho ruim comparado a outros algoritimos.



