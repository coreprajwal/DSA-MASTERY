#Logic of Fibonacci series with recursion


n=int(input("Enter the number: "))

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


print(fibo(n))