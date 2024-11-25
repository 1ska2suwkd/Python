f = open("python/SKU/1학년/2학기/Quiz/Coke/20240861-1.txt",'w')
coke = int(input("Coke count: "))

print(f"Coke count is {coke}.")
f.write(f"Coke count is {coke}.\n")

while(coke):
    money = int(input("Insert money: "))
    print(f"{money} won received")
    f.write(f"{money} won received\n")
    
    if money < 1000:
        continue
    elif money == 1000:
        coke -= 1
    else:
        print(f"Change is {money-1000} won.")
        f.write(f"Change is {money-1000} won.\n")
        coke -= 1

print("Sold out")
f.write("Sold out")

f.close()

