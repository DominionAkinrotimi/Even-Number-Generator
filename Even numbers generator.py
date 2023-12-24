
''' QUESTION
Write a program to generate even numbers between 0 and 1000, the total number of even numbers generated and the average of the even numbers.'''

# METHOD 1
num =0
nums=[]

while num in range (1000):
     num+=2
     if num < 1000:
        nums.append(num)
   
summation = sum(nums) 
length = len(nums)
avg = summation / length 
#print(nums)
print ("method 1")
print(f"sum: {summation}   length: {length}     average: {avg} ")


# METHOD 2
num=0
sum =0
count = 0
for num in range(2,1000,2):
    count += 1
    sum = sum + num
avg = sum/ count
print(" ")
print ("method 2")
print(f"sum: {sum}   length: {count}     average: {avg} ")

