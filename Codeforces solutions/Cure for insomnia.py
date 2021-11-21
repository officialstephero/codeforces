dn_hits = []

for i in range(4):
    a = int(input())
    dn_hits.append(a)

d = int(input())
count_dn = []

for dns in dn_hits:
    n = 0
    hits = []
    while d > n:
        n += dns
        if n <= d:
            hits.append(n)
    count_dn = set.union(set(count_dn), set(hits))

print(len(count_dn))
