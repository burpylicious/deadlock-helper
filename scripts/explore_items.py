import requests
from datetime import datetime, timezone

url = "https://api.deadlock-api.com/v1/assets/items"
response = requests.get(url, timeout=10)

print("Status:", response.status_code)

items = response.json()
print("Items found:", len(items))

print(type(items))
print(type(items[0]))

for item in items:
    if item.get("class_name") == "ability_lash_flog":
        print(item["name"], "-", item["type"], '-', item["hero"], '-', datetime.fromtimestamp(item["update_time"],tz= timezone.utc))
        print(type(item["properties"]))
        item_dmg = item["properties"]['Damage']
        print(item_dmg['value'], ':', type(item_dmg['value']), '-', item_dmg["scale_function"], ':', type(item_dmg["scale_function"]))