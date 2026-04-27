n = input()
cnt = 0
for i in n:
    if i == "4" or i == "7":
        cnt += 1
cnt = str(cnt)
for i in cnt:
    if i not in "47":
        print("NO")
        break
else:
    print("YES")
