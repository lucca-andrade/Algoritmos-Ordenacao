# Merge Sort

def merge_sort(lista):
    if len(lista) <= 1:
        return lista  
    meio = len(lista) // 2  
    esquerda = merge_sort(lista[:meio])  
    direita = merge_sort(lista[meio:])  
    return merge(esquerda, direita)  

def merge(esquerda, direita):
    resultado = []
    i = j = 0   
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1            
    resultado.extend(esquerda[i:])  
    resultado.extend(direita[j:])  
    return resultado

lista = [5, 1, 9, 3, 8, 2]
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)


## VANTAGENS
# Mantém a ordem relativa dos elementos iguais, o que pode ser crucial em certos contextos.

# Funciona bem mesmo quando os dados não cabem inteiramente na memória 
# (como em ordenações externas).

# Funciona melhor que outros algoritmos quando implementado para listas ligadas, 
# já que não precisa de acesso direto por índices.


# DESVANTAGENS
# Usa espaço extra para armazenar sublistas durante a ordenação, tornando-o menos eficiente 
# para listas pequenas.

# A implementação tradicional não ordena diretamente na própria lista e precisa de memória extra.

# Pode exigir mais cópias de elementos, afetando sua eficiência em algumas situações.
