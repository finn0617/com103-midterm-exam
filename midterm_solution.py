heroes = [
    {"name": "Layla", "role": "Marksman"},
    {"name": "Tigreal", "role": "Tank"},
    {"name": "Gusion", "role": "Assassin"},
    {"name": "Kagura", "role": "Mage"},
    {"name": "Chou", "role": "Fighter"}
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

i = 0
while i < len(heroes):
    print(str(i+1) + ". " + heroes[i]["name"] + " [" + heroes[i]["role"] + "]")
    i += 1

print("==========================================\n")

matches = []

match_num = 1
while match_num <= 4:
    print("--- MATCH " + str(match_num) + " ---")
    hero_choice = int(input("Hero number (0 to skip): "))

    if hero_choice == 0:
        print()
        match_num += 1
        continue

    if hero_choice >= 1 and hero_choice <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()
        print()

        # KDA calculation
        if deaths > 0:
            kda = (kills + assists) / deaths
        else:
            kda = (kills + assists) / 1

        # Tag
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        match = {
            "hero": hero_choice - 1,
            "kda": kda,
            "result": result,
            "tag": tag,
            "match_num": match_num
        }

        matches.append(match)

    match_num += 1


# Compute stats
wins = 0
losses = 0

i = 0
while i < len(matches):
    if matches[i]["result"] == "W":
        wins += 1
    else:
        losses += 1
    i += 1

matches_played = len(matches)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
else:
    win_rate = 0


# Find best match manually
best_match = None
i = 0

while i < len(matches):
    if best_match is None:
        best_match = matches[i]
    else:
        if matches[i]["kda"] > best_match["kda"]:
            best_match = matches[i]
    i += 1


# Print results
print("=============================================")
print("     " + ign + " -- MATCH LOG (" + rank + ")")
print("=============================================")

i = 0
while i < len(matches):
    m = matches[i]
    hero_name = heroes[m["hero"]]["name"]

    if m["result"] == "W":
        result_str = "WIN"
    else:
        result_str = "LOSS"

    print("[" + str(m["match_num"]) + "] " + hero_name +
          " | KDA: " + str(round(m["kda"], 2)) +
          " | " + result_str +
          " | " + m["tag"])
    i += 1

print("---------------------------------------------")
print("Matches Played : " + str(matches_played))
print("Wins : " + str(wins) + " | Losses : " + str(losses))
print("Win Rate : " + str(win_rate) + "%")

if best_match is not None:
    best_hero_name = heroes[best_match["hero"]]["name"]
    print("Best Match : [" + str(best_match["match_num"]) + "] " +
          best_hero_name + " (KDA: " + str(round(best_match["kda"], 2)) + ")")

print("=============================================")
