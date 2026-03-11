from functools import reduce, partial, singledispatch, lru_cache
from operator import mul, add


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return (reduce(lambda x, y: add(x, y), spells))
    elif operation == "multiply":
        return (reduce(lambda x, y: mul(x, y), spells))
    elif operation == "max":
        return (max(spells))
    elif operation == "min":
        return (min(spells))
    else:
        return "Invalid Operator"


def partial_enchanter(base_enchanter: callable) -> dict[str, callable]:
    tab = {"Sword": (69, "Thunder Sword", "Lightning"),
           "Shark": (67, "Shork", "Ice"),
           "Fireball": (100, "Fireball", "Fire")}
    return ({
        f"{tab[name][2]}_enchant":
        (partial(base_enchanter, power=tab[name][0],
                 element=tab[name][2],
                 target=tab[name][1])) for name in tab
    })


def enchanter(target: str, power: int, element: str) -> str:
    return (f"{target}: {power} of element {element}")


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatcher(val: any) -> str:
        return "Unknown Type !"

    @dispatcher.register(int)
    def _(val=int):
        return (f"Spell casted dealing {val} damage !")

    @dispatcher.register(str)
    def _(val=str) -> str:
        return (f"Casting spell: {val}")

    @dispatcher.register(list)
    def _(val=list) -> str:
        return (f"casting {val[0]} with a power of {val[1]}")
    return dispatcher


print(f"Adding: {spell_reducer((1, 2, 3, 4), "add")}")
print(f"Multiplying: {spell_reducer((1, 2, 3, 4), "multiply")}")
print(f"Max: {spell_reducer((1, 2, 3, 4), "max")}")
print(f"Min: {spell_reducer((1, 2, 3, 4), "min")}")
print(f"Invalid: {spell_reducer((1, 2, 3, 4), "minus")}")
enchant = partial_enchanter(enchanter)
print(enchant["Lightning_enchant"]())
fib = memoized_fibonacci(30)
print(fib)
print(memoized_fibonacci.cache_info())
dispatcher = spell_dispatcher()
print(dispatcher(69))
print(dispatcher("Blub"))
print(dispatcher(["Fireball", 100]))
