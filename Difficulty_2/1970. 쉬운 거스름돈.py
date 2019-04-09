# 거스름돈 단위를 list로 지정
paper = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
trial = range(int(input()))

for j in trial:
    
    # 회차 출력
    j += 1
    print("#" + "{}".format(j))
    
    # 받은 돈 입력
    N = int(input())
    arr = []
    temp = 0
    
    # 거스름돈 계산
    for i in paper:
        temp = N % i
        N = N // i
        arr.append(str(N))
        N = temp
    
    # 거스름돈 출력
    print(' '.join(arr))

    
    
