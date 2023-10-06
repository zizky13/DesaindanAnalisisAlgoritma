def reccur_fibo(n):
    if n<=1:
        return n
    else:
        return reccur_fibo(n-1) + reccur_fibo(n-2)

nterms = 20

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonnaci sequence: ")
    for i in range (nterms):
        print(reccur_fibo(i))