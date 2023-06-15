n = int(input("Enter number :"))
aux = n
m = [[0 for i in range((n * 2) - 1)] for i in range((n * 2) - 1)]
print(m)

for i in range(n):
    for  l in range(i, (n*2)-1-i):
        for  c in range(i, (n*2)-1-i):
            m[l][c] = n - i
print(m)
for  l in range((n*2)-1):
    for  c in range((n*2)-1):
        print(m[l][c], end='')
    print()