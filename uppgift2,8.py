import random
while True:
    print ("Tärningen är kastad")
    n = random.randint(1,6)
    m = random.randint(1,6)
    print ("Du fick", n, "och", m)
    choice = input ("Vill du köra igen?: ")
    if choice.lower() == ("ja"):
        continue
    else:
        print("FUCK YOU DÅ")
        break