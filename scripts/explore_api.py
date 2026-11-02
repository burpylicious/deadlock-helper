import requests

url = "https://api.deadlock-api.com/v1/assets/heroes"
response = requests.get(url, timeout=10)

print("Status:", response.status_code)

heroes = response.json()
print("Heroes found:", len(heroes))

playable_heroes = []

for hero in heroes:
    if hero["player_selectable"]:
        playable_heroes.append(hero)

for hero in playable_heroes:
    print(hero["name"])

print("Playable heroes:", len(playable_heroes))