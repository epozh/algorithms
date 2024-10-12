import time
import resource
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start = time.time()
import random

f = open("input.txt", "w")
m = [random.randint((-10) ** 3, 10 ** 3) for i in range(0, 1000)]  # генерим 1000 рандомных чисел
for i in m:
    f.write(str(i) + " ")
f.write("\n")
f.write('114')

f = open('input.txt')
a = f.readline().split()
V = f.readline()  # то что надо найти считыаем
f.close()


def search(n):
    b = []  # пустой массив
    x = len(n)
    for i in range(x):  # проходимся по всем элементам массива
        if n[i] == V:  # если элемент равен p
            b.append(i)  # то закидываем элемент в массив
    if len(b) > 0:
        return len(b), b  # возвращает длина массива и сам массив, если массив b не пустой стал
    elif len(b) == 0:  # массив пустой, значит просто выносится -1
        return '-1'


f1 = open('output.txt', 'w')
f1.write(' '.join(map(str, search(a))))
f1.close()
end = time.time() - start
print(end)
print('{}'.format(mem))
