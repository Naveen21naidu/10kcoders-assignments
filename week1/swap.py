#method 2 without using temp (bitwise XOR)
a=5
b=4
a=a^b 
b=a^b
a=a^b
print(f'a:{a},b:{b}')
