s = input().strip()
a = s[0]
op = s[1]
b = s[2]
c = s[4]

def val(ch):
    return int(ch) if ch.isdigit() else None

A = val(a)
B = val(b)
C = val(c)

if a == 'x':
    if op == '+':
        x = C - B
    else:  
        x = C + B

elif b == 'x':
    if op == '+':
        x = C - A
    else:  
        x = A - C

else: 
    if op == '+':
        x = A + B
    else:  
        x = A - B

print(x)