file = input("파일 이름(txt 파일이 아닐 경우 x): ")

if file == "x":
    file = input("파일 이름(파일 확장자까지 명시): ")
else:
    file = file + ".txt"

try:
    f = open(file, "r+", encoding='cp949')  # w+ 모드로 할 경우 파일 자동 생성
except:
    print("파일을 확인하세요.")  # 파일 읽기 오류가 발생하면 실행
else:
    text = f.read()  # 파일 읽기
    while True:

        print("\n1.단어 빈도수 측정 \n2.특정 단어 교체 \n3.파일 복사")
        menu = int(input("\n번호 입력 : "))

        if menu == 1:
            print(text)

            word = input("검색할 단어 입력 : ")
            print("\'{0}\'이 사용된 횟수 = {1}".format(word, text.count(word)))

        elif menu == 2:
            print(text)

            org = input("\n찾을 내용 : ")
            chg = input("바꿀 내용 : ")

            print("%d 번을 모두 바꿉니다." % text.count(org))
            text = text.replace(org, chg)
            f.seek(0)  # 파일 포인터를 처음으로 이동
            f.write(text)  # 파일 수정
        elif menu == 3:
            copy = input("복사할 파일명 : ")

            orgfile = open(file, "rb")
            txt = orgfile.read()
            orgfile.close()

            with open(copy, "wb") as newfile:  # 바이트 단위로 파일 쓰기
                newfile.write(txt)

            print("파일이 복사되었습니다.")

        elif menu == 0:
            print("파일 수정을 끝냅니다.")
            break

        else:
            print("잘못된 번호")

    f.close()
