import random
while True:
    rn = random.randrange(100,1000)
    rn = list(str(rn))
    print("세자리 정수가 랜덤으로 생성되었습니다.")
    if rn[0] == rn[1] or rn[0] == rn[2] or rn[1] == rn[2]:
        continue
    break

while True:
    strike = 0
    ball = 0
    print("세자리 정수 답을 예측해보세요 : ", end = "")
    ans = list(input())

    for i in range(len(ans)):
        if ans[i] in rn and ans[i] == rn[i]:
            strike += 1
        elif ans[i] in rn and ans[i] != rn[i]:
            ball += 1

    print(strike,"strike ,",ball, "ball")

    if strike == 3:
        print("게임을 종료합니다.")
        exit()




