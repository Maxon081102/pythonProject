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


a = [1, 0, 3, 2]
b = []
deg = len(a)
n = 0
while 2 ** n < deg:
    n += 1
n=3
deg = 2 ** n
for i in range(deg - len(a)):
    a.append(0)
rev = calc_rev(deg, n)
print(rev)
w = calc_w(deg)
print(w)


def fft(a, deg, fft):
    if fft == True:
        for i in range(1, len(w) // 2):
            w[i], w[len(w) - 1 - i] = w[len(w) - 1 - i], w[i]
        for i in range(deg):
            a[i] = a[i] / deg
    for i in range(deg):
        if i < rev[i]:
            a[i], a[rev[i] ] = a[rev[i] ], a[i]
    span = 1
    step = deg // 2
    for k in range(n):
        for i in range(0,deg, 2 * span):
            for j in range(span):
                u = i + j
                v = i + j + span
                x = a[u] + a[v] * w[(j * step)%deg]
                y = a[u] + a[v] * w[(j * step + deg // 2)%deg]
                a[u] = x
                a[v] = y
        span *= 2
        step //= 2
    return a
    #res = [0 for i in range(deg)]
    #for i in range(deg):
     #   for j in range(len(a)):
     #       res[i] += a[j] * w[(j * i) % deg]
    #return res


#k = fft(a, deg, True)
k = fft(a, deg, False)
print(k)
