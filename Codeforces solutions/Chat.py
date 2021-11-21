n = input()

unique_elem = []
welcome = "hello "

k = 0

for i in range(len(n)):
    if n[i] == welcome[k]:
        unique_elem.append(n[i])
        k += 1

unique_elem = "".join(unique_elem)

if unique_elem == welcome[:-1]:
    print("YES")
else:
    print("NO")
