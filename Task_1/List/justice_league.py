justice_league = ["Superman", "Batman", "Wonder Women", "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("Number of members:", len(justice_league))
print("Step 1:", justice_league)

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Step 2:", justice_league)

# 3. Move Wonder Women to the begining
justice_league.remove("Wonder Women")
justice_league.insert(0, "Wonder Women")
print("Step 3:", justice_league)

# 4. Move Green Lantern between Aquaman ana Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Step 4:", justice_league)

# 5. Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 5:", justice_league)

# 6. Sort alphabetically
justice_league.sort()

print("Final Justice League:", justice_league)
print("Step 6:", justice_league)
print("New Leader", justice_league[0])



