# test case number
T = int(input())
for r in range(T):

    # number of ingredients(N^2 shape of matrix)
    N = int(input())
    r += 1
    lst = []
    temp_min = 0
    S, U = 0, 0

    # update list values
    for n in range(N):
        a = input().split(' ')
        lst.append(a)

    temp_min = int(lst[0][1]) + int(lst[1][0])

    # investigating minimum value
    for i in range(len(lst)):

        for j in range(len(lst)):

            U = S
            S = int(lst[i][j]) + int(lst[j][i])

            # comparing values
            if (abs(U - S) <= temp_min) & (S != 0):
                temp_min = abs(U - S)

    # 회차출력
    print("#" + "{}".format(r), end=' ');
    print(temp_min)
