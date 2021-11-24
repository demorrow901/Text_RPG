import random


def create_enemy(enemy_final_name): # Генерация имени противника
    enemy_name = ("Иван ", "Василий ", "Инокентий ", "Джейс ", "Виктор ", "Варнер ")
    enemy_surname = ("Петров", "Шакалов", "Нашоров", "Эрондейл", "Аркейнов", "Кирраман")
    enemy_final_name = ""
    enemy_name = random.choice(enemy_name)
    enemy_surname = random.choice(enemy_surname)
    enemy_final_name = enemy_name + enemy_surname

    return enemy_final_name 


def enemy_characteristic(enemy_attack):
    enemy_attack = random.randrange(1, 15)

    return enemy_attack,


