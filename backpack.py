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


import time

def peso(item):
    return item[0]

def valor(item):
    return item[1]

def backpackPD(n, c, itens, stats=None):
    if stats is not None:
        stats['iterations'] = 0
        stats['instructions'] = 0
    
    maxTab = [[0 for j in range(c+1)] for i in range(n+1)]
    if stats is not None:
        stats['instructions'] += (n + 1) * (c + 1)  # Inicialização da matriz
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if stats is not None:
                stats['iterations'] += 1
                stats['instructions'] += 2  # comparação + acesso ao peso
            if peso(itens[i-1]) <= j:
                if stats is not None:
                    stats['instructions'] += 4  # max + 2 acessos + adição
                maxTab[i][j] = max(maxTab[i-1][j], 
                                 valor(itens[i-1]) + maxTab[i-1][j - peso(itens[i-1])])
            else:
                if stats is not None:
                    stats['instructions'] += 1  # atribuição
                maxTab[i][j] = maxTab[i-1][j]
    return maxTab[n][c]

def backpack_brute_force(num, cap, itens, stats=None):
    if stats is not None:
        stats['iterations'] = 0
        stats['instructions'] = 0
    
    def brute_force_recursive(n, c):
        if stats is not None:
            stats['iterations'] += 1
            stats['instructions'] += 2  # if + return
        
        if n == 0 or c == 0:
            return 0
        
        if stats is not None:
            stats['instructions'] += 1  # comparação
        if itens[n-1][0] > c:
            return brute_force_recursive(n-1, c)
        
        if stats is not None:
            stats['instructions'] += 4  # max + adição + 2 chamadas
        return max(itens[n-1][1] + brute_force_recursive(n-1, c - itens[n-1][0]),
                  brute_force_recursive(n-1, c))
    
    return brute_force_recursive(num, cap)

def run_benchmark():
    # Casos de teste
    test_cases = [
        {
            'name': 'Aula (N=10, C=165)',
            'items': list(zip([23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
                            [92, 57, 49, 68, 60, 43, 67, 84, 87, 72])),
            'capacity': 165
        },
        {
            'name': 'Pequeno (N=3, C=2)',
            'items': list(zip([1, 2, 3], [3, 2, 1])),
            'capacity': 2
        },
        {
            'name': 'Similar (N=8, C=100)',
            'items': list(zip([10, 20, 30, 25, 15, 35, 40, 50],
                            [40, 50, 60, 45, 30, 55, 65, 70])),
            'capacity': 100
        }
    ]
    
    algorithms = [
        ('Brute Force', backpack_brute_force),
        ('Dynamic Prog', backpackPD)
    ]
    
    print("\nKnapsack Benchmark Results")
    print("-" * 100)
    print(f"{'Algorithm':<15} {'Test Case':<20} {'Result':>12} {'Iterations':>12} {'Instructions':>12} {'Time (s)':>12}")
    print("-" * 100)
    
    for algo_name, algo_func in algorithms:
        for test in test_cases:
            n = len(test['items'])
            c = test['capacity']
            stats = {'iterations': 0, 'instructions': 0}
            start_time = time.time()
            try:
                result = algo_func(n, c, test['items'], stats)
                end_time = time.time()
                exec_time = end_time - start_time
                print(f"{algo_name:<15} {test['name']:<20} {result:>12} {stats['iterations']:>12} {stats['instructions']:>12} {exec_time:>12.6f}")
            except RecursionError:
                print(f"{algo_name:<15} {test['name']:<20} {'Error':>12} {'N/A':>12} {'N/A':>12} {'N/A':>12}")
        print("-" * 100)

if __name__ == "__main__":
    run_benchmark()