# Testing an elif chain to determine user input.
# Using this test to establish ideas for a text based adventure game.

print("What would you like to do?")
print("explore")
print("camp")
print("fight")
print("")
action = input()

print("")
print(f"you chose {action}")
print("")

if action == "explore":
    print("You find nothing, the dev isn't working very hard is he?")
elif action == "camp":
    print("You make camp, have a good rest.")
elif action == "fight":
    print("There's nothing to fight, the dev isn't working very had is he?")
else:
    print(f"You entered {action}, and we aren't prepared for that input")
