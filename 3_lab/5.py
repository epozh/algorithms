f = open('input.txt')
citiz = list(map(int, f.readline().split(',')))
f.close()


def sorted(citiz):
    for i in range(1, len(citiz)):
        for j in range(i, 0, -1):
            if citiz[j] > citiz[j - 1]:
                citiz[j], citiz[j - 1] = citiz[j - 1], citiz[j]
    return citiz


def hIndex(citiz):
    sorted(citiz)
    n = len(citiz) - 1
    i = 0
    while i < n:
        if citiz[n - i] < i:
            break
        else:
            i += 1
    res = i - 1
    return res


y = hIndex(citiz)
f = open('output.txt', 'w')
f.write(str(y))
