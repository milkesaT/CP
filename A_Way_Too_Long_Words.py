m=int(input())
for s in range(m):
      n=input().strip()
      if len(n)>10:
         print(n[0]+str(len(n)-2)+n[-1])
      else:
           print(n)