## Basic Recursion ,Date:- 29-07-2025


n=int(input("Enter a number to get its factorial:"))

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

print(f"Factorial of {n} is :",factorial(n))