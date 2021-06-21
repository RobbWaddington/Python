# this will be where I build building blocks of a text based game

# stat block

stat_block = {
    "str": 5,
    "wis": 5,
    "chr": 5,
    "lck": 1
}

# character creation

points_to_add = 5

print("Welcome adventurer, what shall we call you?")
print("")

name = input()

print(f"Nice to meet you, {name}. Let's get you some stats!")

print("You have 5 stat points to assign, your base stats are ")
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

health = 100 + (stat_block["str"] * 4)
spell_power = 10 + (stat_block["wis"] * 2)

print(health)
print(spell_power)
