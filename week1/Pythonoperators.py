#Task : 
#how to swap two numbers at least four approaches.

#method 1 without using temp
a=8
b=9
a=a+b 
b=a-b
a=a-b
print(f'a:{a},b:{b}')

#method 2 without using temp (bitwise XOR)
a=5
b=4
a=a^b 
b=a^b
a=a^b
print(f'a:{a},b:{b}')

#method 3 using temp
a=3
b=2
temp=a
a=b
b=temp
print(f'a:{a},b:{b}')

#method 4 
a=1 
b=2 
a,b=b,a 
print(f'a:{a},b:{b}')
