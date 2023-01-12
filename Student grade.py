from random import randint


def Print_Opthions():  # 옵션을 출력해주는 함수

    print("=" * 30)
    print("=" * 30)
    print("1. 개인 점수 조회")
    print("2. 개인 총점/평균 조회")
    print("3. 과목별 총점/평균 조회")
    print("4. 전체 총점/평균 조회")
    print("5. 본인 점수등록")
    print("6. 본인 과목별 등수 확인")
    print("7. 본인 전체 등수 확인")
    print("8. 성적 전체 출력")
    print("=" * 30)
    print("0. 종료")
    print("=" * 30)
    print("=" * 30)


def Menu():
    menu = int(input("실행할 메뉴를 선택해주세요 : "))

    while True:
        if menu == 1:
            Indi_Score()
            Print_Opthions()
            Menu()

        elif menu == 2:
            Indi_Sum_Aver_Score()
            Print_Opthions()
            Menu()

        elif menu == 3:
            Sub_Sum_Aver_Score()
            Print_Opthions()
            Menu()

        elif menu == 4:
            All_Sub_Sum_Aver_Score()
            Print_Opthions()
            Menu()

        elif menu == 5:
            Put_My_Score()
            Print_Opthions()
            Menu()

        elif menu == 6:
            Sub_My_Rank()
            Print_Opthions()
            Menu()

        elif menu == 7:
            All_Sub_My_Rank()
            Print_Opthions()
            Menu()

        elif menu == 8:
            All_Score()
            Print_Opthions()
            Menu()

        elif menu == 0:
            print("프로그램을 종료합니다.")
            break

        else:
            print("존재하지 않는 메뉴입니다. 다시 입력해주세요.")
            Menu()
        break


def Indi_Score():  # 옵션 1. 개인 점수 조회 함수

    score.sort()
    number = int(input("개인 점수를 조회할 학생의 번호를 입력해주세요 : "))

    if number > len(score) or number < 1:  # 존재하지 않는 학생의 번호를 입력할 때, 함수를 재실행
        print("존재하지 않는 학생 번호 입니다. 다시 입력해주세요 ")
        print("\n")
        Indi_Score()

    else:
        i = 0
        while i < len(score):  # 반복문을 통해 입력한 학생의 번호를 구하기
            if i + 1 == number:
                print("[ {} ]번 학생의 국어 성적은 [ {} ]점, 영어 성적은 [ {} ]점, 수학 성적은 [ {} ]점 입니다.".format(number, score[i][1],
                                                                                               score[i][2],
                                                                                               score[i][3]))
                break
            else:
                i += 1


def Indi_Sum_Aver_Score():  # 옵션 2. 개인 총점/평균 조회 함수

    score.sort()
    number = int(input("개인 총점/평균을 조회할 학생의 번호를 입력해주세요 : "))

    if number > len(score) or number < 1:  # 존재하지 않는 학생의 번호를 입력할 때, 함수를 재실행
        print("존재하지 않는 학생 번호 입니다. 다시 입력해주세요 ")
        print("\n")
        Indi_Sum_Aver_Score()
    else:
        i = 0
        while i < len(score):  # 반복문을 통해 입력한 학생의 번호를 구하기
            if i + 1 == number:
                print("[ {} ]번 학생의 총점은 [ {} ]점, 평균은 [ {} ]점 입니다.".format(number, sum(score[i][1:]),
                                                                         round(sum(score[i][1:]) / 3, 2)))
                break
            else:
                i += 1


def Sub_Sum_Aver_Score():  # 옵션 3. 과목별 총점/평균 조회 함수

    score.sort()
    print("과목코드 : 1.국어  2.영어  3.수학")
    cord = int(input("총점/평균을 조회할 과목의 코드를 입력하세요 : "))

    if cord == 1:
        sub_score = 0
        for i in range(len(score)):
            sub_score += score[i][1]

        print("국어 과목의 총점은 [ {} ]점, 평균은 [ {} ]점 입니다.".format(sub_score, round(sub_score / len(score), 2)))

    elif cord == 2:
        sub_score = 0
        for i in range(len(score)):
            sub_score += score[i][2]

        print("영어 과목의 총점은 [ {} ]점, 평균은 [ {} ]점 입니다.".format(sub_score, round(sub_score / len(score), 2)))

    elif cord == 3:
        sub_score = 0
        for i in range(len(score)):
            sub_score += score[i][3]

        print("수학 과목의 총점은 [ {} ]점, 평균은 [ {} ]점 입니다.".format(sub_score, round(sub_score / len(score), 2)))

    else:
        print("과목 코드를 잘못 입력했습니다. 다시 입력해주세요. ")
        print("\n")
        Sub_Sum_Aver_Score()


def All_Sub_Sum_Aver_Score():  # 옵션 4. 전체 총점/평균 조회 함수

    score.sort()
    all_score = 0
    for i in range(3):  # 이중 반복문을 통해 국영수 점수를 모두 더하기
        for j in range(len(score)):
            all_score += score[j][i + 1]

    print("전체 총점은 [ {} ]점, 평균은 [ {} ]점 입니다.".format(all_score, round(all_score / (len(score) * 3), 2)))


def Put_My_Score():  # 옵션 5. 본인 점수 등록

    score.sort()
    print("자신의 점수를 입력하는 메뉴입니다. 번호는 가장 마지막으로 들어가게 됩니다.")

    my_score = []

    i = 0
    for i in range(len(score)):  # 가장 마지막 번호에 자신의 점수를 저장
        i += 1
    my_score.append(i + 1)

    i = 0
    while i < 1:
        rnr_score = int(input("국어 점수를 입력해주세요 : "))
        if rnr_score < 0 or rnr_score > 100:
            print("점수의 범위를 벗어났습니다. 0~100사이의 숫자를 입력해주세요.")
        else:
            my_score.append(rnr_score)
            i += 1

    i = 0
    while i < 1:
        dud_score = int(input("영어 점수를 입력해주세요 : "))
        if dud_score < 0 or dud_score > 100:
            print("점수의 범위를 벗어났습니다. 0~100사이의 숫자를 입력해주세요.")

        else:
            my_score.append(dud_score)
            i += 1

    i = 0
    while i < 1:

        tn_score = int(input("수학 점수를 입력해주세요 : "))

        if tn_score < 0 or tn_score > 100:
            print("점수의 범위를 벗어났습니다. 0~100사이의 숫자를 입력해주세요.")

        else:
            my_score.append(tn_score)
            i += 1

    score.append(my_score)


def Sub_My_Rank():  # 옵션 6. 본인 과목별 등수 확인 함수

    print("과목코드 : 1.국어  2.영어  3.수학")
    cord = int(input("등수를 조회할 과목의 코드를 입력하세요 : "))
    my_number = len(score)

    if cord == 1:
        score.sort(key=lambda x: (-x[1], x[0]))

        for i in range(len(score)):
            if score[i][0] == my_number:
                print("국어 과목의 등수는 [ {} ]명 중 [ {} ]등 입니다.".format(len(score), i + 1))

    elif cord == 2:
        score.sort(key=lambda x: (-x[2], x[0]))

        for i in range(len(score)):
            if score[i][0] == my_number:
                print("영어 과목의 등수는 [ {} ]명 중 [ {} ]등 입니다.".format(len(score), i + 1))

    elif cord == 3:

        score.sort(key=lambda x: (-x[3], x[0]))

        for i in range(len(score)):
            if score[i][0] == my_number:
                print("수학 과목의 등수는 [ {} ]명 중 [ {} ]등 입니다.".format(len(score), i + 1))

    else:
        print("과목 코드를 잘못 입력했습니다. 다시 입력해주세요. ")
        print("\n")
        Sub_My_Rank()


def All_Sub_My_Rank():  # 옵션 7. 본인 전체 등수 확인 함수

    score.sort()
    all_score = []
    for i in range(len(score)):
        SU = [i + 1]
        jumsu = sum(score[i][1:])
        SU.append(jumsu)
        all_score.append(SU)

    my_number = len(score)
    all_score.sort(key=lambda x: (-x[1], x[0]))

    for i in range(len(score)):

        if all_score[i][0] == my_number:
            print("전체 등수는 [ {} ]명 중 [ {} ]등 입니다.".format(len(score), i + 1))


def All_Score():  # 옵션 8. 성적 전체 출력

    score.sort()
    for r in score:
        print(r)

    # ============================================================================== 여기서부터 프로그램 시작


score = []
for i in range(30):  # 2중 반복문을 통해 국,영,수 점수를 랜덤으로 2차원 리스트로 저장
    SU = [i + 1]

    for j in range(3):
        jumsu = randint(0, 100)
        SU.append(jumsu)

    score.append(SU)

Print_Opthions()
Menu()
