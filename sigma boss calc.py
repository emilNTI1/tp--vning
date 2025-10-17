import time
while True:
    print(f"Vilket räknesätt vill du använda?")
    print(f"1. Addition")
    print(f"2. Subtraktion")
    print(f"3. Multiplikation")
    print(f"4. Division")
    val = input(f"(1-4)?: ")
    num1 = float(input(f"num1: "))
    num2 = float(input(f"num2: "))

    if val == "1":
        print(f"= {num1 + num2}")
    elif val == "2":
        print(f"= {num1 - num2}")
    elif val == "3":
        print(f"= {num1 * num2}")
    elif val == "4":
        print(f"= {num1 / num2}")
    elif val == "67":
        print(f"uhmmmmm")
        time.sleep(2)
        print(f"idk bro")
        time.sleep(2)
        print(f"ts too hard")
        time.sleep(2)    
        break
    else:
        print(f"Wow du tog ett annat nummer en fucking 1-4, du är så jävla rolig är du inte det.")
        break