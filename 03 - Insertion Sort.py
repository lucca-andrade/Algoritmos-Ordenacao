# Insertion Sort

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]  
        j = i - 1  
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]  
            j -= 1         
        lista[j + 1] = chave  
    return lista

lista = [5, 1, 9, 3]
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)


## VANTAGENS
# Mantém a ordem relativa de elementos iguais, Tornando-o estável.

# Eficiente para listas pequenas ou quase ordenadas.

# Consegue realizar ordenações online, de forma que ordena elementos à medida que chegam, 
# sem precisar de todos os dados inicialmente.

# Pouco uso de memória: Funciona de forma in-place, ou seja, não requer estruturas de dados adicionais.


## DESVANTAGENS
# Baixa eficiência para grandes conjuntos de dados.

# Realiza muitas movimentações em listas totalmente desordenadas, impactando o desempenho.

# Não é ideal para aplicações que exigem alta velocidade.
