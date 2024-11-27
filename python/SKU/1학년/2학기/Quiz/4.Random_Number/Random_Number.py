f = open("python/SKU/1학년/2학기/Quiz/4.Random_Number/20240861-4.txt",'w')
import random

computer_num = random.randrange(1,101)
cnt = 0
N = 0

print("Computer selected a random number.")
f.write("Computer selected a random number.\n")

while(computer_num != N):
    cnt+=1
    N = int(input("Input your number (1~100): "))
    if N>computer_num:
        print("SMALL")
        f.write("SMALL\n")
    else:
        if N<computer_num:
            print("BIG")
            f.write("BIG\n")

print(f"Bingo! You tried {cnt} times")
f.write(f"Bingo! You tried 3 times.\n")