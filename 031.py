a1 = 10
r = 3
n = 20

pa = a1 + (n - 1) * r

for i in range(a1, pa, r):
    if i <= pa:
        print(i)