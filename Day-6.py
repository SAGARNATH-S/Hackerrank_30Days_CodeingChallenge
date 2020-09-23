n=int(input())
s=[]
for i in range(0,n):
    a=input()
    s.append(a)
for i in s:
    for j in range(0,len(i)):
        if j%2==0:
          print(i[j], end ='')
    print(" ",end='')
    for j in range(0,len(i)):
        if j%2!=0:
          print(i[j], end ='')
    print()
