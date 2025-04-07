import time
#  FIBO-REC (n)
#     se n ≤ 1
#     então devolva n
#     senão a ← FIBO-REC (n − 1)
#           b ← FIBO-REC (n − 2)
#           devolva a + b

def fibo_rec(n, stats=None):
    if stats is not None:
        stats['iterations'] += 1
        stats['instructions'] += 2  # if + return
    
    if n <= 1:
        if stats is not None:
            stats['instructions'] += 1  # comparison
        return n
    
    if stats is not None:
        stats['instructions'] += 1  # return with addition
    return (fibo_rec(n - 1, stats) + fibo_rec(n - 2, stats))


#  FIBO (n)
#      f [0] ← 0
#  f [1] ← 1
#  para i ← 2 até n faça
#          f[i] ← f[i-1]+f[i-2]
#  devolva f [n]

def fibo(n, tab=None, stats=None):
    if stats is not None:
        if 'iterations' not in stats:
            stats['iterations'] = 0
        if 'instructions' not in stats:
            stats['instructions'] = 0
        stats['instructions'] += 1  # if tab is None
    
    if tab is None:
        tab = [-1] * (n + 1)  # Garantir tamanho suficiente
        if stats is not None:
            stats['instructions'] += 1  # array initialization
    
    # Inicializa casos base
    tab[0] = 0
    if stats is not None:
        stats['instructions'] += 1  # assignment
    if n == 0:
        if stats is not None:
            stats['instructions'] += 1  # return
        return 0
    
    tab[1] = 1
    if stats is not None:
        stats['instructions'] += 1  # assignment
    if n == 1:
        if stats is not None:
            stats['instructions'] += 1  # return
        return 1
    
    # Preenche a tabela iterativamente
    for i in range(2, n + 1):
        if stats is not None:
            stats['iterations'] += 1  # Conta cada iteração do loop
            stats['instructions'] += 3  # assignment + addition + loop overhead
        tab[i] = tab[i - 1] + tab[i - 2]
    
    if stats is not None:
        stats['instructions'] += 1  # return
    return tab[n]


#  MEMOIZED-FIBO (f, n)
#   para i ← 0 até n faça
#        f [i] ← −1
#   devolva LOOKUP-FIBO (f, n)
#
#  LOOKUP-FIBO (f, n)
#   se f [n] ≥ 0
#       então devolva f [n]
#   se n ≤ 1
#   então f [n] ← n
#   senão f [n] ← LOOKUP-FIBO(f, n − 1) + LOOKUP-FIBO(f, n − 2)
#   devolva f [n]

def lookup_fibo(f, n, stats=None):
    if stats is not None:
        stats['iterations'] += 1
        stats['instructions'] += 2  # if + return
    
    if f[n] >= 0:
        if stats is not None:
            stats['instructions'] += 1  # comparison
        return f[n]
    
    if n <= 1:
        f[n] = n
        if stats is not None:
            stats['instructions'] += 2  # assignment + return
        return f[n]
    else:
        if stats is not None:
            stats['instructions'] += 3  # assignment + addition + return
        f[n] = lookup_fibo(f, n-1, stats) + lookup_fibo(f, n-2, stats)
        return f[n]

def memoized_fibo(f, n, stats=None):
    if stats is not None:
        stats['instructions'] += 2  # loop setup + return
    
    for i in range(n + 1):
        if stats is not None:
            stats['iterations'] += 1
            stats['instructions'] += 1  # assignment
        f[i] = -1
    return lookup_fibo(f, n, stats)

def run_benchmark():
    test_values = [4, 8, 16, 32, 128, 1000, 10000]
    algorithms = [
        ('Recursive', fibo_rec, [4, 8, 16, 32]),
        ('Dynamic', fibo, [4, 8, 16, 32]),
        ('Memoized', lambda n, stats: memoized_fibo([-1] * (n + 1), n, stats), test_values)
    ]
    
    print("\nFibonacci Benchmark Results")
    print("-" * 100)
    print(f"{'Algorithm':<12} {'Input':>6} {'Result':>12} {'Iterations':>12} {'Instructions':>12} {'Time (s)':>12}")
    print("-" * 100)
    
    for algo_name, algo_func, values in algorithms:
        for n in values:
            stats = {'iterations': 0, 'instructions': 0}
            start_time = time.time()
            try:
                result = algo_func(n, stats)
                end_time = time.time()
                exec_time = end_time - start_time
                print(f"{algo_name:<12} {n:>6} {result:>12} {stats['iterations']:>12} {stats['instructions']:>12} {exec_time:>12.6f}")
            except RecursionError:
                print(f"{algo_name:<12} {n:>6} {'Error':>12} {'N/A':>12} {'N/A':>12} {'N/A':>12}")
        print("-" * 100)

if __name__ == "__main__":
    run_benchmark()