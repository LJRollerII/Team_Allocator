import random

print("Welcome to Team Allocator")

players = ["John",  "Martin", "Whitney",
           "Kendall", "Malcolm", "Denise",
           "Brandon", "Kyle",  "Lucy",
           "Zoey", "Darrell", "Erica",
           "William", "Jean", "LLoyd",
           "Maria", "Anthony","Grace",
           "Natalie", "Xavier", "Amanda",
           "Harold", "Penelope", "Lamar",
           "Carolyn", "Jasper", "Nicole",
           "Orlando", "Trina", "Gary"]

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport? \
        \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//3]
        print("Team 1 captain: " + random.choice(team1))
        print("Team 1: ")
        for player in team1:
            print(player)

        team2 = players[len(players)//3:(len(players)//3)*2]
        print("\nTeam 2 captain: " + random.choice(team2))
        print("Team 2: ")
        for player in team2:
            print(player)

        team3 = players[(len(players)//3)*2:]
        print("\nTeam 3 captain: " + random.choice(team3))
        print("Team 3: ")
        for player in team3:
            print(player)
    else:
        for i in range (0, 30, 2):
            print(players[i] + "vs" + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + "starts")
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
    