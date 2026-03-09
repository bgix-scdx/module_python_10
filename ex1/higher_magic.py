def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined() -> any:
        spell1()
        spell2()
    return combined


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(count) -> None:
        if condition(count) is True:
            spell(count)
        else:
            print("spell fizziled")
    return cast


def hello() -> None:
    print("hello")


def world() -> None:
    print("world")


def display(text: any) -> None:
    print(f"Throwing sharknado spell with a power of {text} strength")


def check(val: int) -> bool:
    return (val == 3)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    basepower = 10
    print(f"{basepower} base power, multiplying by {multiplier}")

    def newfunc() -> None:
        base_spell(basepower * multiplier)
    return (newfunc)


def fireball(strength: int) -> None:
    print(f"A fireball has been casted ({strength} power)")


def icedome(strength: int) -> None:
    print(f"A icedome has been casted ({strength} power)")


def spell_sequence(spells: list[callable]) -> callable:
    def execall(val: any) -> None:
        for i in spells:
            i(val)
    return execall


combiner = spell_combiner(hello, world)
combiner()
caster = conditional_caster(check, display)
caster(1)
caster(3)

megafireball = power_amplifier(fireball, 5)

spellall = spell_sequence((fireball, icedome, fireball))
spellall(5)
