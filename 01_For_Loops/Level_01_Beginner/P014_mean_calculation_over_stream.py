#Given a list of numbers, write a for loop to compute the precise arithmetic mean (average) without using
#built-in sum() or len() functions.

a = [10, 20, 30, 40, 50]
count=0
sum=0
for i in a:
    sum+=i
    count+=1
avg=sum//count
print(avg)