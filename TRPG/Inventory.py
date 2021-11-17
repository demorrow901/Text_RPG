from os import system

"""
TODO

    кол-во одинаковых предметов в инвентаре
    параметр игрока (бартер) снижает цену зелья

"""


def show_location_shop(user_name, user_money, user_inventory):
    is_busy = True
    while is_busy:
        system("cls")
        potion_prise = 500
        print(f"имя {user_name}")
        print(f"деньги {user_money}")
        print(f"инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("-----------")
        print(f"не хотите ли купить зелье{potion_prise}")
        print(f"1 — Купить зелье за {potion_prise}")
        print("2 — Вернуться в лагерь") 

        user_choise = ""
        while user_choise not in ("1", "2"):
                    user_choise = input("что делать?")

        if user_choise == "1" and user_money >= potion_prise:
            user_money -= potion_prise
            user_inventory.append("зелье")
        elif user_choise == "1" and user_money <= potion_prise:
            print("Вам не хватает денег")
            input("ENTER - продолжить")
        else:
            is_busy = False

        return user_money

