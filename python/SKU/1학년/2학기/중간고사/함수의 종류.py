#일반적인 함수
def add1(a,b):
    result = a+b
    return result
a = 3
b = 4
print(add1(a,b))

#입력값이 없는 함수
def say():
    return 'Hi'
print(say())

#리턴값이 없는 함수
def add2(a,b):
    print("%d %d의 합은 %d입니다." %(a,b,a+b))
a = add2(3,4)
