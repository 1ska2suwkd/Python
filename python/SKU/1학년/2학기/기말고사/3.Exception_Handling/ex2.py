#모든 예외 처리
try:
    result = 10/int(input("숫자를 입력하세요: "))
    print(f"결과: {result}")
except Exception as e:
    print(f"예외 발생: {e}")
#Exception class의 객체를 e라는 변수에 담는다.
#as는 별칭을 지정하거나 값을 변수에 담는다는 의미를 가짐