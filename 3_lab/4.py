f = open('input.txt')
s, p = map(int, f.readline().split())
seg = [tuple(map(int, f.readline().split())) for _ in range(s)]
points = list(map(int, f.readline().split()))
f.close()

def counting(seg, points):
    def quick_sort(a):
        if len(a) <= 1:
            return a
        el = a[len(a) // 2][1]
        left = [x for x in a if x[1] < el]
        middle = [x for x in a if x[1] == el]
        right = [x for x in a if x[1] > el]
        return quick_sort(left) + middle + quick_sort(right)
    seg = quick_sort(seg)
    res = [0] * len(points)
    for i, point in enumerate(points):
        c = 0
        for segment in seg:
            if segment[0] <= point <= segment[1]:
                c += 1
            if point >= segment[1] or point <= segment[0]:
                break
        res[i] = c
    return res

res = counting(seg, points)
f = open('output.txt', 'w')
f.write(" ".join(map(str, res)))
