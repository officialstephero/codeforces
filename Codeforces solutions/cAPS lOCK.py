s = input()

lowercase = [s for s in s if s.islower()]

if (s[0].islower() is True) and (len(lowercase) == 1):
    print(s.title())
elif len(lowercase) == 0:
    print(s.lower())
else:
    print(s)
