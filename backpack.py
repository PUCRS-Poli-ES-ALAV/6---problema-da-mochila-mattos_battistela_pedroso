#  1. Resolva o problema da mochila conforme o enuciado em sala de aula.
#
#     1. Ache uma solução que testa todas as combinações possíveis e seleciona a melhor, aplicando divisão-e-conquista ou não;
#     1. Contabilize o número de iterações;
#     1. Implemente e teste sua solução, para o caso exposto em aula e outros de mesmo porte (;-)).
#
#  1. Resolva o problema da mochila utilizando o algoritmo com programação dinâmica visto em aula, teste e contabilize o número de iterações.
#  Inteiro backPackPD(Inteiro N, Inteiro C, Tupla<Inteiro, Inteiro> itens)
#     N = número de produtos;
#     C = capacidade real da mochila
#     itens[N +1];   // (O índice 0 guarda null), Tupla com peso e valor
#     maxTab[N+1][C+1];
#
#     Inicialize com 0 toda a linha 0 e também a coluna 0;
#     para i = 1 até N
#        para j = 1 até C
#           se item itens[i].peso <= j // se o item cabe na mochila atual
#              maxTab[i][j] = Max(maxTab[i-1][j],
#                                 itens[i].valor +
#                                   maxTab[i-1][j – itens[i].peso]);
#           senão
#              maxTab[i][j] = maxTab[i-1][j];
#
#     retorne maxTab[N][C] // valor máximo para uma mochila de capacidade C e
#                          //que pode conter itens que vão do item 1 até o item N.

def peso(item):
    return item[0]

def valor(item):
    return item[1]

def backpackPD(n, c, itens):
    maxTab = [[0 for j in range(c+1)] for i in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if peso(itens[i-1]) <= j:
                maxTab[i][j] = max(maxTab[i-1][j], valor(itens[i-1]) +
                                   maxTab[i-1][j - peso(itens[i-1])])
            else:
                maxTab[i][j] = maxTab[i-1][j]
    return maxTab[n][c]

def backpack_brute_force(num, cap, itens):
    if num == 0 or cap == 0:
        return 0
    
    if itens[num-1][0] > cap:
        return backpack_brute_force(num-1, cap, itens)
    
    else:
        return max(itens[num-1][1] + backpack_brute_force(num-1, cap-itens[num-1][0], itens),
                   backpack_brute_force(num-1, cap, itens))


def backpack_brute_force_loops(num, cap, itens):
    max_value = 0
    for i in range(1<<num):
        value = 0
        weight = 0
        for j in range(num):
            if i & (1<<j):
                value += itens[j][1]
                weight += itens[j][0]
        if weight <= cap and value > max_value:
            max_value = value
    return max_value


def backpack_divide_conquer(num, cap, itens):
    if num == 0 or cap == 0:
        return 0
    
    if itens[num-1][0] > cap:
        return backpack_divide_conquer(num-1, cap, itens)
    
    else:
        take = itens[num-1][1] + backpack_divide_conquer(num-1, cap-itens[num-1][0], itens)
        skip = backpack_divide_conquer(num-1, cap, itens)
        return max(take, skip)


def main():
    pesos   = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    valores = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    items = list(zip(pesos, valores))
    #  print(items)
    #  a = backpackPD(len(items), 165, items)
    #  b = backpack_brute_force(len(items), 165, items)
    #  c = backpack_divide_conquer(len(items), 165, items)
    #  print(a)
    #  print(b)
    #  print(c)

    p2 = [1, 2, 3]
    v2 = [3, 2, 1]
    i2 = list(zip(p2, v2))
    d = backpackPD(len(i2), 2, i2)
    print(d)

main()
