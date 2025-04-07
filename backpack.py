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
    # Casos de teste fornecidos
    test_cases = [
        {
            'name': 'Caso 1 (N=10, C=165)',
            'items': list(zip([23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
                            [92, 57, 49, 68, 60, 43, 67, 84, 87, 72])),
            'capacity': 165,
            'expected_blocks': [1, 2, 3, 4, 6],  # Índices 1-based: 1, 2, 3, 4, 6
            'expected_value': 309  # 92 + 57 + 49 + 68 + 43
        },
        {
            'name': 'Caso 2 (N=6, C=190)',
            'items': list(zip([56, 59, 80, 64, 75, 17],
                            [50, 50, 64, 46, 50, 5])),
            'capacity': 190,
            'expected_blocks': [1, 2, 5],  # Índices 1-based: 1, 2, 5
            'expected_value': 150  # 50 + 50 + 50
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
                
                # Verifica se o resultado está correto
                status = "OK" if result == test['expected_value'] else "FAIL"
                print(f"{algo_name:<15} {test['name']:<20} {result:>12} {stats['iterations']:>12} {stats['instructions']:>12} {exec_time:>12.6f} {status}")
            except RecursionError:
                print(f"{algo_name:<15} {test['name']:<20} {'Error':>12} {'N/A':>12} {'N/A':>12} {'N/A':>12} FAIL")
        print("-" * 100)

if __name__ == "__main__":
    run_benchmark()