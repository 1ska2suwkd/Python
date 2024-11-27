cnt = 0
sum = 0

while cnt != 5:
    N = int(input("input number(> 10): "))
    if N <= 10:
        print("Give me bigger one. (> 10)")
        continue
    sum+=N
    cnt+=1

print(f"sum= {sum} , avg= {sum/5}")