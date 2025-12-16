N = int(input("Enter N: "))

if N >= 1:
    total = sum(range(1, N + 1))   
else:
    total = sum(range(N, 2))    
    
print(total)