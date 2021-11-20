import os #copy
import potion_shop_copy


user_resistanse = 1 # Сопротивляемость персонажа к урону(персонаж получает меньше урона)
user_vitality = 5 # живучесть персонажа (напрямую влияет на количество здоровья) 
user_luck = 1 # удача персонажа (влияет на удачу персонажа(с большей вероятностью может появится случайное событие и др))
user_eloquence = 1 # навык красноречия (влияет на общение(торговец может сделать скидку и др.))
user_stamina = 1 # выносливость персонажа (влияет на возможность владеть некоторой экипировкой)
user_dexterity = 1 # ловкость персонажа (влияет на возможность владеть некоторой экипировкой и на шанс уклонения)
user_forse = 1 # сила персонажа (влияет на возможность владеть некоторой экипировкой и на силу атаки)
user_hp = user_vitality * 20
user_xp = 0
user_name = "Вася"
user_money = 5000
user_level = 1
user_inventory = []
user_inventory.append("Меч")
user_inventory.append("Щит")
game = True


def show_location_home(game, user_hp,user_xp,user_name, user_money, user_inventory):
    while game:
        os.system("cls")
        print(f"{user_name} сидит на базе")
        print(f"Имя {user_name}")
        print(f"Деньги: {user_money}") # TODO при возвращении на базу, у персонажа восстанавливаются деньги
        print(f"Инвентарь:")
        for item in user_inventory:
            print("•", item)
        print("-----------")
        print(f"1 - Пойти в магазин")
        print(f"2 - Выйти из игры")

        user_choise = ""
        user_choise = input("Что делать? ")

        if user_choise == "1":
            potion_shop_copy.show_location_shop(user_name, user_money, user_inventory)
        elif user_choise == "2":
            game = False
        else:
            print("Напишите цифру варианта действия")
            input("ENTER - продолжить")


show_location_home(game, user_hp, user_xp, user_name, user_money, user_inventory)
