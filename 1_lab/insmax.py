import time
import resource
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start = time.time()
import random

f = open("input.txt", "w")
f.write("1000")
f.write("\n")
m = [random.randint((-10) ** 9, 10 ** 9) for i in range(0, 1000)]  # генерим 1000 рандомных чисел
for i in m:
    f.write(str(i) + " ")


f = open('input.txt')
n = int(f.readline())
s = f.readline()
f.close()
x = ([int(i) for i in s.split()])


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and key > arr[i]:
            t = arr[i]
            arr[i] = key
            arr[i + 1] = t
            i = i - 1
    return arr


result = insertion_sort(x)
f = open('output.txt', 'w')
f.write(' '.join(map(str, result)))
f.close()
end = time.time() - start
print(end)
print('{}'.format(mem))
