x = []

for num in "".join([str(i) for i in range(1, 124)]):
    if int(num) != 9:
        x.append(num)

print("".join(x))
