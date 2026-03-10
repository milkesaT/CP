n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
l,r=0,0
s=[]
while(l<len(arr1) and r<len(arr2)):
    if(arr1[l]<arr2[r]):
        s.append(arr1[l])
        l+=1
    else:
        s.append(arr2[r]) 
        r+=1

if(l<n):
    s.extend(arr1[l:])
if(r<m):
    s.extend(arr2[r:])
print(*s)

         