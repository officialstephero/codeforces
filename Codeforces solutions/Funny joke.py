f_name = input()
s_name = input()
c_name = input()

d_name = sorted(f_name + s_name)

if d_name == sorted(c_name):
    print('YES')
else:
    print('NO')
