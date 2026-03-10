n=int(input())
reg = [input().strip().lower() for i in range(n)]

counts={}
for name in reg:
    if name not in counts:
        counts[name]=0
        print("OK")
    else:
        counts[name]+=1
        new_name = f"{name}{counts[name]}"
        counts[new_name]=0
        print(new_name)
      