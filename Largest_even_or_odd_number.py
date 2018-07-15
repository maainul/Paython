# take input how many number you want to add
n = int(input('Enter number of elements:'))
# declear a variable name b to store value of elements
b = []
# for lop to take n number of elements
for i in range (0, n):
  a = int(input('Element:'))
  b.append(a) # append method add value into the list
# declear variable for store list of odd and even
even = []
odd =  []
# this for loop is check whether the number is odd or even
for i in b:
  if(i % 2 == 0):
    even.append(i)# store element on the even variable
  else:
    odd.append(i)# store element on the odd variable
# short even number and odd number small to larger
even.sort()
odd.sort()
# store even number or odd number
even_count= 0
odd_count = 0
# count the number of even or odd number
for k in even:
  even_count+=1
for j in odd:
  odd_count+=1
# print the largest even number
print("Largest even number:",even[even_count-1])
print("Largest odd number",odd[odd_count-1])
