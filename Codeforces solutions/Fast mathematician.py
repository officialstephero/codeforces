first_numb = input()
second_numb = input()
third_numb = []
for i in range(len(first_numb)):
    if first_numb[i] == second_numb[i]:
        third_numb.append('0')
    else:
        third_numb.append('1')
print("".join(third_numb))
