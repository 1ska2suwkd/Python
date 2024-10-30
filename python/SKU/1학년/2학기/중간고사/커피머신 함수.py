f = open("C:/tmp/20240861.txt",'w')

def coffee_machine(coffee):
	while True:

		ans = input("커피를 시키시겠습니까?(y또는 n): ")

		if ans == 'y':
			coffee -=1
			print("커피를 제공합니다. (남은 커피 수량: %d)" %coffee)
			f.write("커피를 제공합니다. (남은 커피 수량: %d)\n" %coffee)
		else:
			break
		if coffee == 0:
			print("커피가 다 떨어졌습니다.")
			f.write("커피가 다 떨어졌습니다.\n")
			break

coffee_machine(5)


f.close()
