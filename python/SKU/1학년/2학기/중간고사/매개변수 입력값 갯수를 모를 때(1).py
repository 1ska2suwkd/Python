def add_many(*args):
    result = 0
    for i in args:
        result+=i
    return result
result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
