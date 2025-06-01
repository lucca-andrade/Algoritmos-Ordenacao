# Counting Sort

def counting_sort(lista):
    val_max = max(lista)
    count = [0] * (val_max + 1)
    for num in lista:
        count[num] += 1
    lista_ordenada = []
    for i in range(len(count)):
        lista_ordenada.extend([i] * count[i])   
    return lista_ordenada

# lista = [4, 2, 8, 3, 1]
lista = [4, 9, 10, 23, 40]
print("Lista Ordenada:", counting_sort(lista))


## VANTAGENS
# Alta eficiência para casos onde o número de elementos é grande 
# e o intervalo dos valores é relativamente pequeno.

# Mantém a ordem relativa dos elementos com valores iguais.

# Ele não usa comparações para ordenar os valores.

# Ideal para inteiros pequenos dentro de um intervalo conhecido e limitado.

# Quando combinado com outros algoritmos como Radix Sort, ele pode ser usado 
# para ordenar múltiplos atributos complexos.


# DESVANTAGENS
# Ineficiente para intervalos muito grandes, porque o Counting Sort se torna 
# impraticável devido à alocação de grandes estruturas.

# Não funciona para dados não inteiros (Em casos que envolvam números decimais ou strings, 
# será necessário que os valores sejam convertidos).

# Menos flexível que outros algoritmos, com seu uso sendo limitado a dados 
# com um domínio pequeno e conhecido.
