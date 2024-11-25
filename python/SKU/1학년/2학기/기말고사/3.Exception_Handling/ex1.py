#기본 예외 처리
try:
    x = int(input("숫자를 입력하세요: "))
    result = 10/x
    print(f"결과: {result}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("유효한 숫자를 입력하세요.")