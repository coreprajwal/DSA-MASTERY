## power for a positive integer


x=int(input("put x: "))
n=int(input("put n: "))


def power(x,n):
    if n!=0:
        return x*power(x,n-1)
    else:
        return 1

print(power(x,n-1))