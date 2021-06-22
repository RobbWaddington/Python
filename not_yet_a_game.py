# this will be where I build building blocks of a text based game

class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk


# stat block

stat_block = {
    "str": 5,
    "wis": 5,
    "chr": 5,
    "lck": 1,
    "health": 100,
    "mana": 10
}

# character creation

points_to_add = 5

print("Welcome adventurer, what shall we call you?")
print("")

name = input()


print(f"Nice to meet you, {name}. Choose a difficulty!")
print("easy, medium, hard, or impossible")
difficulty_choice = input()

while True:
    if difficulty_choice == "easy":
        print("Easy it is!")
        points_to_add = 15
        break
    elif difficulty_choice == "medium":
        print("Medium, just right.")
        points_to_add = 10
        break
    elif difficulty_choice == "hard":
        print("Hard for a challenge.")
        points_to_add = 5
        break
    elif difficulty_choice == "impossible":
        print("Impossible, why would you do this?")
        points_to_add = 0
        break
    else:
        print("You have made an invalid choice. Defaulting to Hard.")
        break

print(f"You have {points_to_add} stat points to assign, your base stats are ")
print(stat_block)

while points_to_add > 0:
    print("Where would you like to add points?")

    point_add_location1 = input()

    if point_add_location1 == "str":
        while True:
            print(f"How many points? You have {points_to_add} left.")
            str_add = int(input())
            if str_add > points_to_add:
                print("You don't have that many points to add.")
            else:
                points_to_add = points_to_add - str_add
                old_str = stat_block["str"]
                new_str = str_add + old_str
                stat_block.update({"str": new_str})
                print(f"Your new str value is {new_str}")
                print(stat_block)
                break
    elif point_add_location1 == "wis":
        while True:
            print(f"How many points? You have {points_to_add} left.")
            wis_add = int(input())
            if wis_add > points_to_add:
                print("You don't have that many points to add.")
            else:
                points_to_add = points_to_add - wis_add
                old_wis = stat_block["wis"]
                new_wis = wis_add + old_wis
                stat_block.update({"wis": new_wis})
                print(f"Your new wis value is {new_wis}")
                print(stat_block)
                break
    elif point_add_location1 == "chr":
        while True:
            print(f"How many points? You have {points_to_add} left.")
            chr_add = int(input())
            if chr_add > points_to_add:
                print("You don't have that many points to add.")
            else:
                points_to_add = points_to_add - chr_add
                old_chr = stat_block["chr"]
                new_chr = chr_add + old_chr
                stat_block.update({"chr": new_chr})
                print(f"Your new chr value is {new_chr}")
                print(stat_block)
                break
    elif point_add_location1 == "lck":
        while True:
            print(f"How many points? You have {points_to_add} left.")
            lck_add = int(input())
            if lck_add > points_to_add:
                print("You don't have that many points to add.")
            else:
                points_to_add = points_to_add - lck_add
                old_lck = stat_block["lck"]
                new_lck = lck_add + old_lck
                stat_block.update({"lck": new_lck})
                print(f"Your new lck value is {new_lck}")
                print(stat_block)
                break
    else:
        print("You have not selected a valid stat.")
# stats dependant on stats
print("")
print("Applying stats:")

health_new = 100 + (stat_block["str"] * 4)
spell_power_new = 10 + (stat_block["wis"] * 2)

stat_block.update({"health": health_new})
stat_block.update({"mana": spell_power_new})

print(stat_block)
print("")
print("Suddenly, A FIGHT")

first_enemy = Enemy(5, 1)

print("The enemy is weakened from a previous encounter")
print("Its health is:")
print(first_enemy.hp)
print("Its attack is:")
print(first_enemy.atk)

print("What will you do?")
print("attack, run")

combat_choice = input()

while True:
    if combat_choice == "attack":
        first_enemy.hp = first_enemy.hp - stat_block["str"]
        if first_enemy.hp <= 0:
            print("you win!")
        else:
            print("The enemy survives")
        break
    elif combat_choice == "run":
        print("You get away safely")
        break
    else:
        print("you did not make a valid choice, you die")
        break
