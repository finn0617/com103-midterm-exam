heroes = [
    {"name": "Layla", "role": "Marksman"},
    {"name": "Tigreal", "role": "Tank"},
    {"name": "Gusion", "role": "Assassin"},
    {"name": "Kagura", "role": "Mage"},
    {"name": "Chou", "role": "Fighter"}
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n" + "=" * 42)
print("   MOBILE LEGENDS -- HERO ROSTER")
print("=" * 42)
for i, hero in enumerate(heroes, 1):
    print(f" {i}. {hero['name']:<11} [{hero['role']}]")
print("=" * 42 + "\n")

matches = []
for match_num in range(1, 5):
    print(f"--- MATCH {match_num} ---")
    hero_choice = int(input("Hero number (0 to skip): "))
    
    if hero_choice == 0:
        print()
        continue
    
    if 1 <= hero_choice <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()
        print()
        
        # Calculate KDA
        denominator = deaths if deaths > 0 else 1
        kda = (kills + assists) / denominator
        
        # Determine tag
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"
        
        matches.append({
            "hero": hero_choice - 1,
            "kda": kda,
            "result": result,
            "tag": tag,
            "match_num": match_num
        })

wins = sum(1 for m in matches if m["result"] == "W")
losses = sum(1 for m in matches if m["result"] == "L")
matches_played = len(matches)
win_rate = int(wins / matches_played * 100) if matches_played > 0 else 0
best_match = max(matches, key=lambda m: m["kda"]) if matches else None

# Print match log
print("=" * 45)
print(f"     {ign} -- MATCH LOG ({rank})")
print("=" * 45)

for m in matches:
    hero_name = heroes[m["hero"]]["name"]
    result_str = "WIN" if m["result"] == "W" else "LOSS"
    print(f"[{m['match_num']}] {hero_name:<11} | KDA: {m['kda']:.2f}  | {result_str:<4} | {m['tag']}")

print("-" * 45)
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if best_match:
    best_hero_name = heroes[best_match["hero"]]["name"]
    print(f"Best Match     : [{best_match['match_num']}] {best_hero_name}  (KDA: {best_match['kda']:.2f})")

print("=" * 45) 
