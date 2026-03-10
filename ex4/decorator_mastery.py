from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wraper() -> any:
        spell_timer.__name__ = func.__name__
        t1 = time.time()
        print("Casting", spell_timer.__name__)
        func()
        print("Spell completed:",
              (time.time() - t1), "seconds")
    return wraper


def power_validator(min_power: int) -> callable:
    def spell_func(func: callable) -> callable:
        @wraps(func)
        def wraper(self: any = None, name: str = None,
                   power: int = 0) -> str:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, name, power)
        return wraper
    return spell_func


def retry_spell(max_attempts: int) -> callable:
    def retry(func: callable) -> callable:
        @wraps(func)
        def wrap() -> str:
            for i in range(max_attempts):
                try:
                    return func()
                except ValueError:
                    print("Spell failed, retrying...")
            return f"Spell casting failed after {max_attempts} attempts"
        return (wrap)
    return (retry)


@spell_timer
def Fireball():
    for i in range(0):
        continue
    print("Fireball casted !")


@power_validator(10)
def Cast(self: any, name: str, power: int) -> str:
    return f"{name} of power {power} has been cast !"


@retry_spell(3)
def three_spell() -> str:
    raise ValueError


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            print("The mage's name is too short.")
            return False
        for i in name:
            if str(i).isdigit():
                print("A mage name can not have a number.")
                return False
        print(f"{name} was allowed in the guild.")
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


print(MageGuild.validate_mage_name("Baka"))
print(MageGuild.validate_mage_name("GeGe 7"))
print(three_spell())
print(Cast(name="Dust Devil", power=15))
print()
Fireball()
mage = MageGuild()
print(mage.cast_spell("Curse", 15))
print(mage.cast_spell("Dart", 5))
