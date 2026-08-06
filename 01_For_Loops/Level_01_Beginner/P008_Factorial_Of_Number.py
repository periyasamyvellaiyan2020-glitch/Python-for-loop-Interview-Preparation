#Given a non-negative integer N, compute its factorial (N!) using a for loop. Return 1 if N = 0.
n=int(input("Enter n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)