#Given two integers start and end, along with a divisor K, count how many integers in the range [start, end] are divisible by K using a for loop.
start=int(input('Enter the start value:'))
end=int(input('Enter the End value:'))
k=int(input('Enter the divisor value:'))
count=0
for i in range(start,end+1):
    if(i%k==0):
        count+=1
print(f"{count} digits are in given range")