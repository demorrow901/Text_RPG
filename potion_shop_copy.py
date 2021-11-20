from os import system #copy

"""
TODO
    кол-во одинаковых предметов в инвентаре
    параметр игрока (eloquence) снижает цену зелья
"""


def show_location_shop(user_name, user_money, user_inventory):
    is_busy = True
    potion_prise = 500
    while is_busy:
        system("cls")
        print(f"Имя {user_name}")
        print(f"Деньги {user_money}")
        print(f"Инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("-----------")
        print(f"Не хотите ли купить зелье за {potion_prise} монет")
        print(f"1 — Купить зелье за {potion_prise}")
        print("2 — Вернуться в лагерь") 

        user_choise = ""
        user_choise = input("Что делать? ")

        if user_choise == "1":
            if user_money >= potion_prise:
                user_money -= potion_prise
                user_inventory.append("Зелье восстановления здоровья")
            else:
                print("У Вас не хватает денег")
                input("ENTER - продолжить")
        elif user_choise == "2":
            is_busy = False
        else:
            print("Напишите цифру варианта действия")
            input("ENTER - продолжить")
    return user_money