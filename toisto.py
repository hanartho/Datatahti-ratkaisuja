s = input()
maksimi = count = 0
current = ''
for c in s:
    if c == current:
        count += 1
    else:
        count = 1
        current = c
    maksimi = max(count, maksimi)

print(maksimi)    
