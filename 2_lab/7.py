f = open('input.txt')
n = int(f.readline())
s = f.readline()
f.close()
x = ([int(i) for i in s.split()])

def F(A):
    max_sum = A[0]
    sums = A[0]
    i0, end_index = 0,0

    for i in range(1, len(A)):
        if A[i] > (sums + A[i]):
            sums = A[i]
            i0 = i
        else:
            sums += A[i]
        if sums > max_sum:
            max_sum = sums
            end_index = i
    return A[i0:end_index+1]

itog = F(x)
f = open('output.txt', 'w')
if sum(itog) == 0:
    f.write(str(max(x)))
f.write(' '.join(map(str, itog)))