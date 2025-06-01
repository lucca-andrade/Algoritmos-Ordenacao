# Heap Sort

def heapify(lista, n, i):
    maior = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2   
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  
        heapify(lista, i, 0)  

lista = [4, 10, 3, 5, 1]
heap_sort(lista)
print("Lista ordenada:", lista)


## VANTAGENS
# Sua performance não depende dos dados estarem ordenados ou não, 
# oferecendo uma garantia de desempenho.

# Ele não necessita de memória extra significativa.

# É uma ótima opção para ordenar grandes quantidades de dados.

# Como usa a estrutura de heap, é ideal para algoritmos que envolvem 
# filas de prioridade


## DESVANTAGENS
# A ordem relativa de elementos iguais pode ser alterada.

# A reconstrução do heap exige algumas operações que podem impactar a performance.

# Embora tenha complexidade similar, na maioria dos casos o QuickSort é mais rápido.
