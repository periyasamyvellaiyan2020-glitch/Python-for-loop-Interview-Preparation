#Given an upper limit N, print all odd numbers from 1 to N inclusive using the step parameter of a for loop
#without using an if statement.
n=int(input("Enter n:  "))
for i in range(1,n+1,2):
    print(i)