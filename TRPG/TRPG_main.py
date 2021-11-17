import os
import Inventory

user_hp = 100
user_xp = 0
user_name = "Вася"
user_money = 5000
user_level = 1
user_inventory = []
user_inventory.append("Меч")
user_inventory.append("Щит")
game = True


def show_location_home(game, user_hp,user_xp,user_name, user_money,user_inventory):
    while game:
        print(f"{user_name} сидит на базе")
        print(f"Имя {user_name}")
        print(f"Деньги: {user_money}")
        print(f"Инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("-----------")
        print(f"1 - Пойти в магазин")
        print(f"2 - Выйти из игры")

        user_choise = ""
        while user_choise not in ("1", "2"):
            user_choise = input("Что делать? ")

        if user_choise == 1:
            Inventory.show_location_shop(user_name, user_money, user_inventory)
        else:
            game = False


show_location_home(game, user_hp,user_xp,user_name, user_money,user_inventory)
