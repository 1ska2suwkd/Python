#c언어와 다르게 파이썬은 return을 두 개 이상 할 수 있다. 
def add_and_mul(a,b):
    return a+b,a*b
result = add_and_mul(3,4)
print(result)

result1,result2 = add_and_mul(3,4)
print(result1)
print(result2)
