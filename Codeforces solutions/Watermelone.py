w = input()

import math

if float(w) > 2:
    if math.fmod(int(w), 2) == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
