A = input().strip()
count = 0

for i in range(len(A) - 4):
    if A[i:i+5] == ">>-->" or A[i:i+5] == "<--<<":
        count += 1
print(count)