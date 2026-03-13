#revise the nested for loop and practice problem solving questions till we covered
#reverse a string 
s=input()
rev=''
for ch in s:
    rev=ch+rev 
print(rev)

#slicing
print(s[::-1])

#nested loop 


n=6
for i in range(n):
    for j in range(n-1,-1,-1):
        print(i,j)
    print() 
