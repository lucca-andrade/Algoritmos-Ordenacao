# Bucket Sort

def bucket_sort(lista, num_buckets=5):
    if not lista:
        return []
    
    val_min, val_max = min(lista), max(lista)
    range_val = (val_max - val_min) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    for num in lista:
        indice = int((num - val_min) / range_val)
        if indice == num_buckets:  
            indice -= 1
        buckets[indice].append(num)

    lista_ordenada = []
    for bucket in buckets:
        lista_ordenada.extend(sorted(bucket))  
    return lista_ordenada

lista = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.61]
print("Lista Ordenada:", bucket_sort(lista))


## VANTAGENS
# Eficiente para conjuntos de dados uniformemente distribuídos.

# Boa performance com números decimais/floats, especialmente útil 
# para ordenar números em um intervalo limitado.

# Como os baldes são independentes, é possível ordenar cada balde 
# simultaneamente.


## DESVANTAGENS
# Se os dados não forem distribuídos uniformemente, pode levar a um desempenho ruim.

# Requer memória adicional para armazenar os baldes, o que pode ser um problema 
# em situações de grande volume de dados.

# Definir corretamente a quantidade e os intervalos dos baldes pode ser complexo 
# e pode impactar diretamente na eficiência do algoritmo.

