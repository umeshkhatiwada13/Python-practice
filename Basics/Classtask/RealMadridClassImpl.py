from FootballerClass import Footballer

ronaldo = Footballer("C. Ronaldo", 38, "Portugal", "Striker", True)
ramos = Footballer("Ramos", 36, "Portugal", "Defender", True)

print("Ramos plays as a : {}".format(ramos.position))
print("Age of Ronaldo is : {}".format(ronaldo.age))

squad = [Footballer("C. Ronaldo", 38, "Portugal", "Striker", True),
         Footballer("Ramos", 37, "Portugal", "Defender", True),
         Footballer("Asensio", 27, "Spain", "Forward", False),
         Footballer("Kroos", 33, "Germany", "Midfielder", True)
         ]

for player in squad:
    print("{0},{1} plays as {2}.".format(player.name, player.age, player.position))
    print(f'{"" if player.is_spanish() else "Non-"}Spanish and {"Starter " if player.is_starter else "From Bench"}')
