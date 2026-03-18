from collections import Counter
m,n= list(map(int,input().split()))
ar1= list(map(int,input().split()))
ar2= list(map(int,input().split()))
c1=Counter(ar1)
c2=Counter(ar2)
tot=0
for key in c1:
        if key in c2:
          tot+=c1[key]*c2[key]
print(tot)
 
