from os import system
import arena_enemy
import random


enemy_final_name = ""
damage_to_the_enemy = 0
damage_to_the_user = 0


def show_location_arena(user_resistanse, user_luck, user_dexterity, user_forse, user_name, user_hp, user_xp, user_level, user_inventory, game):
    enemy_hp = 100
    is_busy = True
    while is_busy:
        system("cls")
        print(f"{user_name} пришел на арену")
        print(f"Здоровье - {user_hp}")
        print(f"Уровень - {user_level}")
        print(f"Инвентарь:")
        for item in user_inventory:
            print(f"•", item)
        print("-----------")

        print("1 - Пойти сражаться")
        print("2 - Вернуться на базу")

        user_choise = ""
        user_choise = input("Что делать? ")

        if user_choise == "1":
            system("cls")
            print(f"Ваш противник - {arena_enemy.create_enemy(enemy_final_name)}") # Имя генерируется случайно в модуле arena_enemy
            print(f"Здоровье противника - {enemy_hp}")
            print(f" 1 - Атаковать первым")
            print(f"2 - Дать противнику атаковать Вас")

            user_choise2 = ""
            user_choise2 = input("Что делать? ")

            
            if user_choise2 == "1": # Если игрок выберет атаковать, то по противнику нанесется урон, иначе противник нанесет урон игроку
                while user_hp == 0 or enemy_hp == 0:
                    print(f"Вы атакуете первым")
                    damage_to_the_enemy = user_forse * random.randrange(1, 10)
                    print(f"Вы нанесли противнику {damage_to_the_enemy} ед. урона")
                    enemy_hp -= damage_to_the_enemy
                    input("ENTER - продолжить")
                game = False

            elif user_choise2 == "2":
                while user_hp == 0 or enemy_hp == 0:
                    print(f"{arena_enemy.create_enemy(enemy_final_name)} атакует первым")
                    damage_to_the_user = arena_enemy.enemy_characteristic(enemy_attack)
                    print(f"Вы получили {damage_to_the_user} ед. урона")
                    user_hp -= damage_to_the_user
                    input("ENTER - продолжить")
                game = False

            else:
                print("Напишите цифру варианта действия")
                input("ENTER - продолжить")


        elif user_choise == "2":
            is_busy = False

        else:
            print("Напишите цифру варианта действия")
            input("ENTER - продолжить")


        return user_hp