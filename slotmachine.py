import time
import random
symbols = ["🍒", "🍉", "⭐", "💎"]

def spin():
    return random.choices(symbols, k=4)

def contains_symbols(result, symbol_set):
    return set(symbol_set).issubset(result)

result = spin()
print(result)

def count_same_symbols(result) -> int:
    return {symbol: result.count(symbol) for symbol in set(result)}
    
balance = 100
while balance > 0:
    print("Lets go gambling!")
    print(f"You currently have {balance}kr")
    pull = input("Tryck på spaken för att snurra: Y/n:")
    if pull.lower() == "n":
        break
    balance -=5
    result = spin()
    counts = count_same_symbols(result)
    print(result)
    
    
    
    if 4 in counts.values():
        balance += 100
        time.sleep(1)
        print("Jackpot på 100 kr tjockis")
    elif 3 in counts.values():
        balance += 20
        time.sleep(1)
        print("Wow 20 kr tjockis")
    else:
        time.sleep(1)
        print("Du fucking suger tjockis")
