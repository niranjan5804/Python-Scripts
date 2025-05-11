from addition import addition
from subtarction import subtraction

a = int(input("Enter A Number :"))
b = int(input("Enter A Number :"))
c = input("Enter a operation symbal :")

if c == '+':    
    addition(a,b)
elif c == '-':
    subtraction(a,b) 
else:
    print("Invalid Symbol")    