S1 = input().strip()
S2 = input().strip()
if len(S1) != len(S2):
    print("NO")
else:
    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in S1:
        freq1[ord(ch) - ord('A')] += 1

    for ch in S2:
        freq2[ord(ch) - ord('A')] += 1

    if freq1 == freq2:
        print("YES")
    else:
        print("NO")