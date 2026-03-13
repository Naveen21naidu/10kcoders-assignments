#practice loops and nested loops revise the class again 
n=int(input())
#for loop
for i in range(n):
    print(i,end=' ')

#nested for
for i in range(n):
    for j in range(i):
        print(i,j)
    print()

#while
total_sum=0
while n>0:
    total_sum+=n 
    n-=1 
print(total_sum)

#break,continue,pass
n=6
for i in range(n):
    if i==3:
        continue
    elif i==2:
        pass 
    if i==(n-1):
        break
    print(i)
   
