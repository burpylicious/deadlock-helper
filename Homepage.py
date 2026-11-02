import streamlit as st

from deadlock_helper.api import fetch_items
from deadlock_helper.scaling import scaled_value
from deadlock_helper.lookup import class_name_search


@st.cache_data(ttl=3600)
def load_items():
    print("Loading items...")
    return fetch_items()

items = load_items()
flog = class_name_search(items, "ability_lash_flog")

flog_damage = flog["properties"]["Damage"]
base_damage = flog_damage["value"]
stat_scale = flog_damage["scale_function"]["stat_scale"]

st.title("Deadlock Helper")
st.write("A beginner's guide to Deadlock's items and abilities.")
st.write("Items loaded:", len(items))
st.write("Found:", flog["name"])

spirit_power = st.slider("Spirit power", min_value=0, max_value=100, value=20)
total_damage = scaled_value(base_damage, spirit_power, stat_scale)

st.metric("Lash · Flog damage", f"{total_damage:.1f}")
st.caption(f"{base_damage} + {spirit_power} × {stat_scale} = {total_damage:.1f}")
st.caption("Numbers from deadlock-api.com, refreshed every hour.")