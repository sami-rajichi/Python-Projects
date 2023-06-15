s = input("Enter a string : ")
count, j, ns = 1, 0, ""

for i in range(1, len(s)):
    if s[i] == ' ':
        ns += '_'
        j += 1
        continue
    if s[i] == s[j]:
        count = count + 1
    else:
        ns += str(count)
        count = 1
    j += 1
ns += str(count)
print(ns)