counter = 0
for i in [1,2]:
    for j in ["cat","bird"]:
        print(f"({i},{j}) - {counter}")
        counter += 1

for k in range(5):
    n1, n2 = 1, 2
    print(n1, n2, end=" ")
    for j in range(1,3 + k):
        s = n1 + n2
        print(s, end=" ")
        n1 = n2
        n2 = s
    print()
