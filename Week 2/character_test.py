from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude?")
dave.set_weakness("cheese")

dave.describe()
dave.talk()

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
