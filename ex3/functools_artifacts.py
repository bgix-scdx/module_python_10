from functools import reduce, partial, wraps
from ex2.scope_mysteries import enchantment_factory

def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return (reduce(lambda x, y: x + y, spells))
    elif operation == "multiply":
        return (reduce(lambda x, y: x * y, spells))
    elif operation == "max":
        return (max(spells))
    elif operation == "min":
        return (min(spells))
    else:
        return "Invalid Operator"


def partial_enchanter(base_enchanter: callable) -> dict[str, callable]

print(f"Adding: {spell_reducer((1, 2, 3, 4), "add")}")
print(f"Multiplying: {spell_reducer((1, 2, 3, 4), "multiply")}")
print(f"Max: {spell_reducer((1, 2, 3, 4), "max")}")
print(f"Min: {spell_reducer((1, 2, 3, 4), "min")}")
print(f"Invalid: {spell_reducer((1, 2, 3, 4), "minus")}")
