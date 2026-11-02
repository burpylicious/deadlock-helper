import requests

from deadlock_helper.lookup import class_name_search
from deadlock_helper.scaling import scaled_value

url = "https://api.deadlock-api.com/v1/assets/items"
response = requests.get(url, timeout=10)
items = response.json()

flog = class_name_search(items, "ability_lash_flog")

flog_damage = flog["properties"]["Damage"]
base_damage = flog_damage["value"]
stat_scale = flog_damage["scale_function"]["stat_scale"]

for spirit_power in [0, 20, 50, 100]:
    print(scaled_value(base_damage, spirit_power, stat_scale))

print(class_name_search(items, "ability_not_real"))