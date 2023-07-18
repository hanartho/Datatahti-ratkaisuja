n = int(input())
list = list(map(int, input().strip().split()))[:n-1]
list.sort()
for i in range(len(list)):
    if i+1 != list[i]:
        puuttuva = i+1
        break
    else:
        puuttuva = n

print(puuttuva)