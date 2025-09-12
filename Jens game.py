namn = input("Vad heter du?: ")
print("Hej", namn, "säger Jens med ett leende")
if len(namn) >= 5:
    print(f"Vi ska börja med en kort uppgift idag, {namn}")
else:
    print(f"Vi ska börja med en lång uppgift idag, {namn}")

print(f"Jens: Vad tycker du om att arbeta med uppgiften, {namn}?")
print(f"1. Jag älskar det!")
print(f"2. Det är okej.")
print(f"3. Jag fucking hatar det.")

val = input("Skriv 1, 2 eller 3: ")

if val == "1":
    print(f"Jens: Vad kul att höra {namn}! Jag stal den från ChatGPT.")
elif val == "2":
        print(f"Jens: Okej {namn}. Föredrar du kanske att arbeta i grupp?")
        if val == "2":
            print("1. Det kan fungera bara inte med Elvira.")
            print("2. Kan vi bara fucking sluta jens?")
            val = input("Skriv 1 eller 2: ")
        if val == "1":
            print(f"Jens: Okej {namn}. Jobba med Wilmer då.")
        elif val == "2":
            print(f"Jens: Aldrig. Blir klar med uppgiften först.")
        elif val.lower() == "auralicious":
            print(f"You aint duke dennis lil bro, go to bed with that shit")
        else:
            print(f"Jens: Prata svenska lil bro.")
        

elif val == "3":
    print(f"Jens: Jag förstår {namn}. Jag tog den ändå från ChatGPT")
elif val.lower() == "auralicious":
    print(f"You aint duke dennis lil bro, go to bed with that shit")
else:
    print(f"Jens: Prata svenska lil bro.")