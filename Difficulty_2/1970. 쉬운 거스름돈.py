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












trial = int(input)
N = int(input)
t = 0

def fun(N):
    num_str = str(N)
    arr = []

    def unit5(num_dep):
        a = int(num_dep) // 5
        arr.append(a)
        b = int(num_dep) % 5
        arr.append(b)

    if len(num_str) >= 5:
        num_dep = num_str[0:-4]
        unit5(num_dep)
        num_dep = num_str[-4: len(num_str)+1]
        unit5(num_dep)
    else:
        for k in range(1: len(num_str)):
        num_dep = num_str[0:len(num_str) - (k - 1)]
        unit5(num_dep)

print(fun(N).arr)


'''  
    if len(num_str) >= 5:
        num_dep = num_str[0:len(num_str)-4]
        unit5(num_dep)
    if len(num_str) >= 4:
        num_dep = num_str[0:len(num_str)-3]
        unit5(num_dep)
    if len(num_str) >= 3:
        num_dep = num_str[0:len(num_str)-2]
        unit5(num_dep)
    if len(num_str) >= 2:
        num_dep = num_str[0:len(num_str)-1]
        unit5(num_dep)

50000 / 32850 ... 32850
10000 / 32850 3 ... 2850
5000  / 2850  ... 2850
1000  / 2850  2 ... 850
500   / 850   1 ... 350
100   / 350   3 ... 50
50    / 50    1 ... 0

trial = int(input)
N = int(input)

N //

'''
trial = input()
N = input()
arr = []
divider = [50000, 10000, 5000, 1000, 500, 100, 50]

def dvd(N):
    for i in len(divider):
        a = N//divider[i]
        b = N%divider[i]
        arr.append(a)
        arr.append(b)
        N = b
for i in range(trial):
    print("#" + (i+1))
    for a in arr:
        print(a)
