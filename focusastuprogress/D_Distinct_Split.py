from collections import Counter
n = int(input())
for _ in range(n):
    length = int(input())
    testcase = input()

    left_set = set()
    right_count =Counter(testcase)
    total_sum = 0

    for c in testcase:
        left_set.add(c)
        right_count[c] -= 1
        if right_count[c] == 0:
            del right_count[c]
        total_sum = max(total_sum, len(left_set) + len(right_count))

    print(total_sum)