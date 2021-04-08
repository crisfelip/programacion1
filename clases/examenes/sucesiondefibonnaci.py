# --- funcion fibo hasta 20 --- #

def fibo(n):
    if n < 2:
        return n
    return fibo(n-1)+fibo(n-2)

for x in range (20):
    print (fibo (x))
