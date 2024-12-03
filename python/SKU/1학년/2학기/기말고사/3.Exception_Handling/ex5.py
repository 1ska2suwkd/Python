try:
    x = int(input("10을 나눌 숫자를 입력: "))
    y = 10 / x
except ZeroDivisionError:
    print("0으로 나누는 것은 불가")
else:
    print(y)
finally:
    print("코드 실행 종료") 