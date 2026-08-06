# Given a positive integer N, calculate and print the sum of all natural numbers from 1 to N using a for loop.
n=int(input("enter n:"))
total=0
for i in range(1,n+1):
      total=total+i
print(total)