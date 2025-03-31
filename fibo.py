#  FIBO-REC (n)
#     se n ≤ 1
#     então devolva n
#     senão a ← FIBO-REC (n − 1)
#           b ← FIBO-REC (n − 2)
#           devolva a + b
def fibo_rec(n):
    if n <= 1:
        return n
    return (fibo_rec(n - 1) + fibo_rec(n - 2))

#  FIBO (n)
#      f [0] ← 0
#  f [1] ← 1
#  para i ← 2 até n faça
#          f[i] ← f[i-1]+f[i-2]
#  devolva f [n]

def fibo(n, tab=[-1] * 10):
    if n == 0:
        tab[0] = 0
        return 0
    elif n == 1:
        tab[1] = 1
        return 1

    tab[n - 1] = fibo(n - 1, tab)
    tab[n - 2] = fibo(n - 2, tab)
    tab[n] = (tab[n - 1] + tab[n - 2])
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

def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    
    if n <= 1:
        f[n] = n
        return f[n]
    else:
        f[n] = lookup_fibo(f, n-1) + lookup_fibo(f, n-2)
        return f[n]


def memoized_fibo(f, n):
    for i in range(n):
        f[i] = -1
    return lookup_fibo(f, n)


def main():
    a = fibo(6)
    b = fibo_rec(6)
    c = memoized_fibo([-1] * 10, 6)
    print(a)
    print(b)
    print(c)




main()

