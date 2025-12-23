x = input().strip()
y = input().strip()

n = len(y)
yy = y + y
count = 0

for i in range(len(x) - n + 1):
    part = x[i:i+n]
    if part in yy:
        count += 1

print(count)