from random import shuffle


players = [input("Mängija 1 nimi: "), input("Mängija 2 nimi: ")]
points = {player: 0 for player in players}

rounds_to_win = 3
rounds_played = 0

while max(points.values()) < rounds_to_win and rounds_played < 10: 
    rounds_played += 1
    print("\nVoor", rounds_played)

    choices = [input(player + ", vali kivi, käärid või paber: ").lower() for player in players]
    shuffle(choices)

    result = "Viik" if choices[0] == choices[1] else choices[0] + " võidab"
    print("Tulemus:", result)
    
   
    if result.split()[0] in points:
        points[result.split()[0]] += 1


print("\nMäng on lõppenud!")
print("\nMängu tulemused:")
for player, point in points.items():
    print(player + ":", point, "punkti")




