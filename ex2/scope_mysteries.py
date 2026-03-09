def magecounter() -> callable:
    count = 0

    def add() -> int:
        nonlocal count
        count += 1
        print(f"Counting: {count}")
        return count
    return add


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power
    print(f"Spell basepower: {power}")

    def newfunc(ammount: int) -> int:
        nonlocal power
        power += ammount
        print(f"Spell power: {power}")
        return power
    return newfunc


def enchantment_factory(enchantement_type: str) -> callable:
    prefix = enchantement_type
    print(f"Enchant prefix: {prefix}")

    def newfunc(item: str) -> str:
        print(f"{prefix} {item}")
        return f"{prefix} {item}"
    return newfunc


def memory_vault() -> callable:
    vault = dict()

    def store(key: str, value: any) -> None:
        vault.update({key: value})
        print(f"{value} has been stored as {key}")

    def recall(key: str) -> any:
        print(f"Fetching: {key}")
        if vault.get(key) is not None:
            return vault.get(key)
        else:
            return "Memory not found."
    return (store, recall)


counter = magecounter()
for i in range(5):
    counter()
print()
accumulator = spell_accumulator(10)
accumulator(10)
print()
enchant = enchantment_factory("Bubbling")
enchant("shark")
print()
store, recall = memory_vault()

store("Key", "Bakus")
print(recall("Key"))
print(recall("Shakys"))
