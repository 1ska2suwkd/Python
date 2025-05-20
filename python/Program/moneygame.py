import os

def main_screen():
    while True:
        os.system('clear')
        print("우리는 세계 평화를 위해 오늘도 돈을 모아야한다.")
        print(f"money : {int(my_status.money)}원")
        
        make_money = input("'z'를 입력해서 돈을 긁어모으자!\n")

        if make_money == 'z':
            my_status.money += 10 * 1.5**(my_status.money_power-1)
        elif make_money == 'store':
            store_screen()
        elif make_money == 'end':
            break

def store_screen():
    while True:
        os.system('clear')
        prise = 10 ** my_status.money_power
        print(f"어서오세요~ 세계 종말을 막기위한 moneystore 입니다!\nmoney : {int(my_status.money)}원")
        print(f"1. money Power Up! : {prise}원\t 2. 돈 벌러 가기")
        choice = input()
        if choice == '1':
            my_status.money_powerLevelUP()
            my_status.money -= prise
        elif choice == '2':
            return # main_screen 함수로 돌아감

class Status:
    def __init__(self,money = 0,money_power = 1):
        self.money = money
        self.money_power = money_power

    def money_powerLevelUP(self):
        self.money_power+=1

my_status = Status()
main_screen()
