#revise operators | evenodd | swap numbers 

a=int(input())
b=int(input())

#evenodd
if a%2==0:
    print(f'{a} is Even')
else:
    print(f'{a} is Odd')
if b%2==0:
    print(f'{b} is Even')
else:
    print(f'{b} is Odd')
    
#swap XOR
a=a^b
b=a^b
a=a^b
print(f'a:{a},b:{b}')

#operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#logical operators
if (a and b)>0:
    print(f'{a},{b} are positive numbers')
else:
    print(f'{a},{b} are Negative numbers')
    
#Relational operators 
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
