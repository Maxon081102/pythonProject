import math


def calc_rev(deg, n):
    rev = [0 for i in range(deg)]
    for i in range(deg):
        for k in range(n):
            if (i & (1 << k)):
                rev[i] ^= 1 << (n - k - 1)
    return rev


def calc_w(deg):
    z = []
    for i in range(deg):
        z.append(complex(math.cos(i * 2 * math.pi / deg), math.sin(i * 2 * math.pi / deg)))
    return z


a = []
b = []
deg = len(a) * len(b)
n = 0
while 2 ** n < deg:
    n += 1
n = 3
deg = 2 ** n
rev = calc_rev(deg, n)
print(rev)
w = calc_w(deg)
print(w)

for i in range(deg):
    if i < rev[i]:
        a[i], a[rev[i]] = a[rev[i]], a[i]
