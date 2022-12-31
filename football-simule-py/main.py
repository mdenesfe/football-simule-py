import random
import time

team1 = input("Kadronuzu içeren dosyanın adını girin: ")
team2 = input("Kadronuzu içeren dosyanın adını girin: ")

team1_name = input("Takımınızın adını girin: ")
team2_name = input("Takımınızın adını girin: ")


def get_form_factor():
    return random.uniform(0, 1)

with open(team1 +".txt") as file:
    team1_players = []
    for line in file:
        name, age, number, position, attack, defense, midfield = line.strip().split(",")
        form_factor = get_form_factor()
        team1_players.append({
            "name": name,
            "age": int(age),
            "number": int(number),
            "position": position,
            "attack": int(attack) * form_factor,
            "defense": int(defense) * form_factor,
            "midfield": int(midfield) * form_factor
        })
    len1 = len(team1_players)
    if len1 != 11:
        print(team1_name + " Hükmen yenildi, skor 0 - 3")
        exit()
        
with open(team2 +".txt") as file:
    team2_players = []
    for line in file:
        name, age, number, position, attack, defense, midfield = line.strip().split(",")
        form_factor = get_form_factor()
        team2_players.append({
            "name": name,
            "age": int(age),
            "number": int(number),
            "position": position,
            "attack": int(attack) * form_factor,
            "defense": int(defense) * form_factor,
            "midfield": int(midfield) * form_factor
        })
    len2 = len(team2_players)
    if len2 != 11:
        print(team2_name + " Hükmen yenildi, skor 3 - 0")
        exit()

team1_attack = 0
team1_defense = 0
team1_midfield = 0

for player in team1_players:
    age = player["age"]
    if age < 25:
        player["age factor"] = 1
    elif age < 30:
        player["age factor"] = 0.9
    elif age < 35:
        player["age factor"] = 0.8
    else:
        player["age factor"] = 0.7

for player in team1_players:
    if player["position"] == "forward":
        team1_attack += player["attack"]
    elif player["position"] == "defender":
        team1_defense += player["defense"]
    elif player["position"] == "midfielder":
        team1_midfield += player["midfield"]

for player in team1_players:
    player["attack"] *= player["age factor"]
    player["defense"] *= player["age factor"]
    player["midfield"] *= player["age factor"]


team2_attack = 0
team2_defense = 0
team2_midfield = 0

for player in team2_players:
    age = player["age"]
    if age < 25:
        player["age factor"] = 1
    elif age < 30:
        player["age factor"] = 0.9
    elif age < 35:
        player["age factor"] = 0.8
    else:
        player["age factor"] = 0.7

for player in team2_players:
    if player["position"] == "forward":
        team2_attack += player["attack"]
    elif player["position"] == "defender":
        team2_defense += player["defense"]
    elif player["position"] == "midfielder":
        team2_midfield += player["midfield"]
for player in team2_players:
    player["attack"] *= player["age factor"]
    player["defense"] *= player["age factor"]
    player["midfield"] *= player["age factor"]


team1_score = (team1_attack + team1_defense + team1_midfield) / 3
team2_score = (team2_attack + team2_defense + team2_midfield) / 3

team1_score = random.gauss(team1_score, 10)
team2_score = random.gauss(team2_score, 10)

print("-----------------------------------")
print("-----------Maç başlıyor-----------")
print("-----------------------------------")
time.sleep(0.9)

team1_goal_chance = team1_attack / (team1_attack + team2_defense)
team2_goal_chance = team2_attack / (team1_defense + team2_attack)

team1_goals = 0
team2_goals = 0

while random.random() < team1_goal_chance:
  team1_goals += 1

  # Choose a random player from the team who is not a goalkeeper
  scorer = random.choice([player for player in team1_players if player["position"] != "goalkeeper"])

  print("GOOOOOLLLL!!! {} {} ile golü buldu!".format(team1_name, scorer["name"], scorer["number"]))
  print("-----------------------------------")
  time.sleep(0.9)

while random.random() < team2_goal_chance:
  team2_goals += 1

  # Choose a random player from the team who is not a goalkeeper
  scorer = random.choice([player for player in team2_players if player["position"] != "goalkeeper"])

  print("GOOOOOLLLL!!! {} {} ile golü buldu!".format(team2_name, scorer["name"], scorer["number"]))
  print("-----------------------------------")
  time.sleep(0.9)


print("İlk yarı bitti, skor {} - {}".format(team1_goals, team2_goals))
print("-----------------------------------")

time.sleep(0.9)

team1_goal_chance = team1_attack / (team1_attack + team2_defense)
team2_goal_chance = team2_attack / (team1_defense + team2_attack)

while random.random() < team1_goal_chance:
    team1_goals += 1
    scorer = None
    for player in team1_players:
        if player["attack"] == max(player["attack"] for player in team1_players):
            scorer = player
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team1_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)

while random.random() < team2_goal_chance:
    team2_goals += 1
    scorer = None
    for player in team2_players:
        if player["attack"] == max(player["attack"] for player in team2_players):
            scorer = player
            break
    print("GOOOOOLLLL!!! {} {} ({}) ile golü buldu!".format(team2_name, scorer["name"], scorer["number"]))
    print("-----------------------------------")
    time.sleep(0.9)

print("İkinci yarı bitti, skor {} - {}".format(team1_goals, team2_goals))
print("-----------------------------------")

if team1_goals > team2_goals:
    print("{} kazandı!".format(team1_name))
elif team1_goals < team2_goals:
    print("{} kazandı!".format(team2_name))
else:
    print("Maç berabere!")
