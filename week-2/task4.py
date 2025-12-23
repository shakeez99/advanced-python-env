x, y = map(int, input().split())
text = input().strip()
original = set()
for i in range(x - y + 1):
    original.add(text[i:i+y])

print(len(original))