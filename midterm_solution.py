# midterm exam - mobile legemds match log
heroes = [
    ["Layla", "Marksman"],
    ["Tigreal", "Tank"],
    ["Gusion", "Assassin"],
    ["Kagura", "Mage"],
    ["Chou", "Fighter"]
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for i in range(len(heroes)):
    print(f" {i+1}. {heroes[i][0]:<10} [{heroes[i][1]}]")

print("==========================================\n")

match_logs = []
wins = 0
losses = 0

for match in range(1, 5):
    print(f"--- MATCH {match} ---")
    hero_num = int(input("Hero number (0 to skip): "))

    if hero_num == 0:
        print()
        continue

    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()

        
        if deaths == 0:
            deaths = 1

        kda = (kills + assists) / deaths

        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        if result == "W":
            wins += 1
            result_text = "WIN"
        else:
            losses += 1
            result_text = "LOSS"

        match_logs.append({
            "hero": heroes[hero_num - 1][0],
            "kda": kda,
            "result": result_text,
            "tag": tag
        })

    print()

matches_played = len(match_logs)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
else:
    win_rate = 0

best_kda = 0
best_index = 0

for i in range(len(match_logs)):
    if match_logs[i]["kda"] > best_kda:
        best_kda = match_logs[i]["kda"]
        best_index = i

print("=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i in range(len(match_logs)):
    m = match_logs[i]
    print(f"[{i+1}] {m['hero']:<10} | KDA: {m['kda']:.2f} | {m['result']} | {m['tag']}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if matches_played > 0:
    best_match = match_logs[best_index]
    print(f"Best Match     : [{best_index+1}] {best_match['hero']}  (KDA: {best_match['kda']:.2f})")

print("=============================================")

# Match input loop added
# final output and summary
