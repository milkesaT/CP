n=int(input())
count=0
for i in range(n):
    problem=list(map(int, input().split()))
    
    count_one=problem.count(1)   
    if ((count_one)>=2):
           count += 1
print(count)

