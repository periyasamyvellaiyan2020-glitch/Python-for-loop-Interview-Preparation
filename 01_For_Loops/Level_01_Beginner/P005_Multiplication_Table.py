 #Given an integer N, generate its multiplication table from 1 to 10. Print each iteration in the exact format: N x
#i = Result.
n=int(input("Enter n:"))
result=1
for i in range(1,11):
    result=i*n 
    print(f"{n} * {i} = {n*i}")