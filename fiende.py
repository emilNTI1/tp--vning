import random
gustav = 100
elvira = 100
print("Du är ute i skolans korridorer och vandrar, men plötsligt...")
print("Du bevittnar två bögar som ska slåss")

while True:
    elvira_attack = random.randint(10, 15)
    gustav_attack = random.randint(1, 30)
    elvira -= gustav_attack
    gustav -= elvira_attack
    print(f"Elvira kallar Gustav för lgbtq slurs för {elvira_attack} dmg")
    print(f"Gustav kastar sin skoterhjälm för {gustav_attack} dmg")
    print(f"Elvira har {elvira}hp kvar, och Gustav {gustav}hp")
    if 68 <= elvira <= 73:
        print("OMG JAG HAR SNART 67HP!!!!!!! - säger Elvira")
        print("Fucking kys Elvira - säger du")
    elif 68<= gustav <=73:
        print("Omg six seven grabbar haha - säger Gustav")
        print("Bro you're not funny gangalang - säger du")
    elvira_attack = random.randint(20, 30)
    gustav_attack = random.randint(1, 100)
    elvira -= gustav_attack
    gustav -= elvira_attack
    print(f"Elvira kastar sin fanta exotic på Gustav för {elvira_attack} dmg")
    print(f"Gustav taffsar på Elviras husdjur för {gustav_attack} dmg")
    print(f"Elvira har {elvira}hp och Gustav {gustav}hp")
    if 0>= elvira:
        print(f"Elvira har 0hp och hon fucking ligger död")
    else:
        elvira_attack = random.randint(100, 1000)
        gustav_attack = random.randint(1, 100)
        elvira -= gustav_attack
        gustav -= elvira_attack
        print(f"Elvira skjuter sin Desert Eagle 50AE kula på Gustav för {elvira_attack} dmg")
        print(f"Gustav sliter ut Elviras strupe för {gustav_attack} dmg")
        print(f"Elvira har {elvira}hp och Gustav {gustav}hp")
        if 0>= gustav and 0>= elvira:
            print(f"Båda har 0hp kvar och dem fucking dödar varandra")
        elif 0>= gustav:
            print(f"Gustav har 0hp och är fucking död")
        elif 0>= elvira:
            print(f"Elvira har 0hp och hon fucking ligger död")
        break