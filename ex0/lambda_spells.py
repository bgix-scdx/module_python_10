def spell_transformer(spell: list[dict]) -> list[str]:
    return list(map(lambda t: f"* {t} *", spell))


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": max(mages, key=lambda dats: dats["power"])["power"],
            "min_power": min(mages, key=lambda dats: dats["power"])["power"],
            "avg_power":
            round(100 * sum(dats["power"] for dats in mages)/len(mages))/100}


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda dats: dats["power"] >= min_power, mages))


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda dats: dats["power"]))


spells = ("Fireballs", "Thunder Strike", "Chicken Nugget")
mages = ({"name": "James", "power": 66}, {"name": "Bonut", "power": 54.05})
artifacts = ({"name": "Fireball", "power": 15, "element": "fire"},
             {"name": "ThunderBolt", "power": 5, "element": "thunder"},
             {"name": "Last Prism", "power": 30, "element": "crystal"})
spell = spell_transformer(spells)
magestat = mage_stats(mages)
powers = power_filter(mages, 50)
sortedartifact = artifact_sorter(artifacts)
print("\n".join(spell))
print(magestat)
print(powers)
for value in sortedartifact:
    print(f"{value["name"]}: {value["power"]} power, "
          f"{value["element"]} element")
