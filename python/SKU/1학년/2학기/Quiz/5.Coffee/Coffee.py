f = open("python/SKU/1학년/2학기/Quiz/5.Coffee/20240861-5",'w')

Coffee = int(input("Coffee count: "))

print(f"Coffee count is {Coffee}.")
f.write(f"Coffee count is {Coffee}.\n")

while(Coffee):
    money = int(input("insert money: "))
    
    print(f"{money} won received.")
    f.write(f"{money} won received.\n")
    
    if money > 1000:
        Coffee-=1
        print(f"Change is {money-1000} won.")
        f.write(f"Change is {money-1000} won.\n")
    else:
        if money<1000:
            continue
        else:
            if money == 1000:
                Coffee-=1

print("Sold out.")
f.write("Sold out.")