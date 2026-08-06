#Given an integer N, find the sum of all numbers between 1 and N inclusive that are divisible by 3 or 5, but not by both.
n=int(input("Enter n:"))
total=0
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        if i%15!=0:
            total=total+i          
print(total)
