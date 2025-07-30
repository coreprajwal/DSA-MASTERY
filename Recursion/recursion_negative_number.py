## Power of a negative number

x=int(input("Enter x: "))
n=int(input("Enter n: "))

def power(x,n):
    if n!=0:
        return x*power(x,n+1)
    else:
        return 1


print(power(x,n))