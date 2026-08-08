#Given an integer N > 1, determine whether it is a prime number using a for loop running up to ⌊√N⌋. Print
#True if prime, False otherwise. 
N=int(input("Enter N more than 1:"))
import math
count=0
sq=math.floor( math.sqrt(N))
for i in range(2,sq+1):
    if N%i==0:
        count+=1
if count==0:
    print("True")
else:
    print("False")






