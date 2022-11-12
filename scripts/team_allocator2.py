import random

print("Welcome to Team Allocator")

players = []

number_of_players = int(input("How many players \
are there? "))
for i in range(1, number_of_players + 1):
    players.append(i)

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport? \
        \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//2]
        print("Team 1 captain: " + str(random.choice(team1)))
        print("Team 1: ")
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]
        print("\nTeam 2 captain: " + str(random.choice(team2)))
        print("Team 2: ")
        for player in team2:
            print(player)

    else:
        for i in range (0, number_of_players, 2):
            print(str(players[i]) + "vs" + str(players[i+1]))
            start = random.randrange(i, i+2)
            print(str(players[start]) + "starts")
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
