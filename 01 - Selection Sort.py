# Selection Sort

def selection_sort(lista):
    numero_elementos = len(lista)
    for i in range(numero_elementos):
        indice_minimo = i
        for j in range(i + 1, numero_elementos):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

lista = [4, 2, 1, 3, 5]
# lista = [(3, "X"), (3, "Y"), (2, "A"), (1, "B"), (2, "C")]  Exemplo de lista "problemática"
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)


## VANTAGENS:
# O Selection Sort é simples e fácil de entender, muito vantajoso e útil para iniciantes.

# Usa pouca memória.

# Funciona bem em listas pequenas, e é uma ótima opção para ambientes de baixo consumo de recursos.

# Ele não precisa que a lista esteja em ordem, já que sempre vai percorrer ela inteira.


## DESVANTAGENS: 
# Muito lento quando usado com listas grandes, já que percorre a lista inteira comparando cada elemento entre si.

# Não é estável, já que realiza trocas independentes da posição original dos elementos iguais, gerando uma ordem errada.
# (Algumas versões mais recentes do Python parecem consertar esse problema, mas o código ainda tem essa falha).

# Não possuí muitas aplicações e é raramente usado.
