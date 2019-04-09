paper = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
trial = range(int(input()))

for j in trial:

    j += 1
    print("#" + "{}".format(j))

    N = int(input())
    arr = []
    temp = 0
    for i in paper:
        temp = N % i
        N = N // i
        arr.append(str(N))
        N = temp

    print(' '.join(arr))