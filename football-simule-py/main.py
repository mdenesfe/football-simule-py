from data import read_players_data, get_team_players, calculate_team_ratings
import random
import time

team1_name = input("Takımınızın adını girin: ")
team2_name = input("Takımınızın adını girin: ")

players = read_players_data('players.csv')

team1_players = get_team_players(players, team1_name)
team2_players = get_team_players(players, team2_name)

if len(team1_players) != 11 or len(team2_players) != 11:
    print("Hükmen yenildi")
    exit()

positions = {
    "forward": "attack",
    "defender": "defense",
    "midfielder": "midfield"
}

team1_attack, team1_defense, team1_midfield = calculate_team_ratings(team1_players, positions)
team2_attack, team2_defense, team2_midfield = calculate_team_ratings(team2_players, positions)

team1_score = (team1_attack + team1_defense + team1_midfield) / 3
team2_score = (team2_attack + team2_defense + team2_midfield) / 3

team1_score = random.gauss(team1_score, 10)
team2_score = random.gauss(team2_score, 10)

print("-----------------------------------")
print("-----------Maç başlıyor-----------")
print("-----------------------------------")
time.sleep(0.9)

for player in team1_players:
    player["fatigue"] = 0
for player in team2_players:
    player["fatigue"] = 0

team1_goal_chance = (team1_attack + team1_midfield) / (team2_midfield + team2_defense)
team2_goal_chance = (team2_attack + team2_midfield) / (team1_defense + team1_midfield)

team1_goals = 0
team2_goals = 0

while random.randint(-100,100) < team1_goal_chance - team2_goal_chance:
    team1_goals += 1
    scorer = None
    for player in team1_players:
        scorer = random.choice(team1_players)
        while scorer["position"] == "goalkeeper":
            scorer = random.choice(team1_players)
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team1_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)
    for player in team1_players:
        if player != scorer:
            player["fatigue"] += 10
    for player in team2_players:
        player["fatigue"] += 5

while random.randint(-100,100) < team2_goal_chance - team1_goal_chance:
    team2_goals += 1
    scorer = None
    for player in team2_players:
        scorer = random.choice(team2_players)
        while scorer["position"] == "goalkeeper":
            scorer = random.choice(team2_players)
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team2_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)
    for player in team2_players:
        if player != scorer:
            player["fatigue"] += 10
    for player in team1_players:
        player["fatigue"] += 5


print("İlk yarı bitti, skor {} - {}".format(team1_goals, team2_goals))
print("-----------------------------------")

time.sleep(0.9)

team1_goal_chance = (team1_attack + team1_midfield) / (team2_midfield + team2_defense)
team2_goal_chance = (team2_attack + team2_midfield) / (team1_defense + team1_midfield)

while random.randint(-100,100) < team1_goal_chance - team2_goal_chance:
    team1_goals += 1
    scorer = None
    for player in team1_players:
        scorer = random.choice(team1_players)
        while scorer["position"] == "goalkeeper":
            scorer = random.choice(team1_players)
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team1_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)
    for player in team1_players:
        if player != scorer:
            player["fatigue"] += 10
    for player in team2_players:
        player["fatigue"] += 5

while random.randint(-100,100) < team2_goal_chance - team1_goal_chance:
    team2_goals += 1
    scorer = None
    for player in team2_players:
        scorer = random.choice(team2_players)
        while scorer["position"] == "goalkeeper":
            scorer = random.choice(team2_players)
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team2_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)
    for player in team2_players:
        if player != scorer:
            player["fatigue"] += 10
    for player in team1_players:
        player["fatigue"] += 5
        
print("İkinci yarı bitti, skor {} - {}".format(team1_goals, team2_goals))
print("-----------------------------------")

if team1_goals > team2_goals:
    print("{} kazandı!".format(team1_name))
elif team1_goals < team2_goals:
    print("{} kazandı!".format(team2_name))
else:
    print("Maç berabere!")