n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
    
    
    
    
    
    
    
    
    
    
    
## OUTPUT:

Case 1:
Enter any number: 6
The number is a Perfect number!
 
Case 2:
Enter any number: 25
The number is not a Perfect number!
