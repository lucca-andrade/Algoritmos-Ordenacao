# Radix Sort

def counting_sort(lista, posicao_decimal):
    n = len(lista)
    lista_ordenada = [0] * n
    count = [0] * 10

    for num in lista:
        indice = (num // posicao_decimal) % 10
        count[indice] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // posicao_decimal) % 10
        lista_ordenada[count[indice] - 1] = lista[i]
        count[indice] -= 1
        i -= 1
    for i in range(n):
        lista[i] = lista_ordenada[i]


def radix_sort(lista):
    val_max = max(lista)
    posicao_decimal = 1
    while val_max // posicao_decimal > 0:
        counting_sort(lista, posicao_decimal)
        posicao_decimal *= 10

lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(lista)
print("Lista Ordenada:", lista)


## VANTAGENS
# Ordenação estável.

# Sem comparações diretas: Organiza números com base nos dígitos individuais, 
# evitando comparações entre eles.

# Eficiente para números inteiros grandes, especialmente quando o intervalo 
# de valores é significativo.

# Bom desempenho em hardware moderno, além de conseguir ser pareado com 
# outros algoritmos para maior eficiência.


# DESVANTAGENS
# Limitado a números inteiros.

# Requer uma lista auxiliar (count e lista_ordenada) para armazenar 
# a ordenação temporária.

# A performance depende da quantidade de dígitos do maior número, 
# podendo se tornar menos eficiente em números com muitos dígitos.

# Menos flexível que algoritmos de comparação como o Quick Sort e Merge Sort.
# (que podem ser aplicados a diversos tipos de dados como strings, números decimais, etc.)


