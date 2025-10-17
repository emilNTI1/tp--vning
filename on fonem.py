import random
import time

def guess_number():
    secret = random.randint(1, 20)
    tries = 5
    print("Gissa numret mellan 1 och 20. Du har", tries, "försök.")
    for i in range(tries):
        try:
            g = int(input(f"Försök {i+1}: "))
        except ValueError:
            print("Skriv ett heltal.")
            continue
        if g == secret:
            print("Rätt! Bra jobbat.")
            return
        print("För högt." if g > secret else "För lågt.")
    print("Du suger, numret var", secret)

def rps():
    choices = {"1":"sten","2":"sax","3":"påse"}
    win = {"sten":"sax","sax":"påse","påse":"sten"}
    print("Sten(1) Sax(2) Påse(3)")
    me = choices.get(input("Ditt val (1-3): ").strip())
    if not me:
        print("Ogiltigt val.")
        return
    comp = random.choice(list(choices.values()))
    print("Du:", me, "– Datorn:", comp)
    if me == comp:
        print("Oavgjort.")
    elif win[me] == comp:
        print("Du vinner!")
    else:
        print("Datorn vinner, fuck you.")

def scramble():
    words = ["aura", "hockey", "skyblock", "zesty", "gay", "homosexuell", "skibidi"]
    w = random.choice(words)
    scrambled = "".join(random.sample(w, len(w)))
    print("Gissa ordet:", scrambled)
    guess = input("Din gissning: ").strip().lower()
    if guess == w:
        print("Rätt!")
    else:
        print("Fel, fuck you. Rätt ord var:", w)

def menu():
    while True:
        print("\n-- Auralicious games --")
        print("1. Gissa numret")
        print("2. Sten-Sax-Påse")
        print("3. Bokstavsblandning")
        print("4. Avsluta")
        choice = input("Välj (1-4): ").strip()
        if choice == "1":
            guess_number()
        elif choice == "2":
            rps()
        elif choice == "3":
            scramble()
        elif choice == "4":
            print("Fuck you")
            break
        else:
            print("Prata svenska lil bro.")
if __name__ == "__main__":
    menu()