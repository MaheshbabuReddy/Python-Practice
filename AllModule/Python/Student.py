from datetime import datetime

class Player:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.matchesPlayed = 0
        self.halfCenturies = 0
        self.centuries = 0
        self.dateOfBirth = ""


def main():
    N = int(input("Enter the number of players: "))

    players = [Player() for _ in range(N)]

    # Read player details
    for i in range(N):
        print(f"Enter details for Player {i + 1}:")
        players[i].name = input("Name: ")
        players[i].country = input("Country: ")
        players[i].matchesPlayed = int(input("Matches Played: "))
        players[i].halfCenturies = int(input("Half Centuries: "))
        players[i].centuries = int(input("Centuries: "))
        players[i].dateOfBirth = int(input("Date of Birth (yyyy): "))

    # Task 1: Find players with the maximum number of centuries
    maxCenturies = max(player.centuries for player in players)
    print("Players with the maximum number of centuries:")
    for player in players:
        if player.centuries == maxCenturies:
            print(player.name)

    # Task 2: Print name and total score for each player
    print("Name and Total Score (Half Centuries + Centuries):")
    for player in players:
        totalScore = player.halfCenturies * 50 + player.centuries * 100
        print(f"{player.name}: {totalScore}")

    # Task 3: Players born between 1991 and 2001 with at least 10 centuries
    print("Players born between 1991 and 2001 with at least 10 centuries:")
    found = False
    for player in players:
        birthYear = player.dateOfBirth
        if 1991 <= birthYear <= 2001 and player.centuries >= 10:
            print(f"{player.name} (Matches Played: {player.matchesPlayed})")
            found = True
    if not found:
        print("-1")

    # Task 4: Players from INDIA and their present age
    print("Players from INDIA and their present age:")
    current_date = 2023
    for player in players:
        if player.country == "INDIA":
            # Calculate present age
            birthYear = player.dateOfBirth
            age = current_date - birthYear
            print(f"{player.name} (Age: {age})")


if __name__ == "__main__":
    main()

