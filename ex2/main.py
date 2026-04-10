from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    for class_name in EliteCard.__bases__:
        method_list = [
            k
            for k, v in vars(class_name).items()
            if not k.startswith("_") and callable(v)
        ]
        print(f"- {class_name.__name__}: {method_list}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity=Rarity.RARE,
        attack=5,
        health=4,
        mana=6,
    )

    print("Combat phase:")
    enemy = EliteCard(
        name="Enemy",
        cost=4,
        rarity=Rarity.COMMON,
        attack=3,
        health=3,
        mana=2,
    )
    attack_result = arcane_warrior.attack(enemy)
    print(f"Attack result: {attack_result}")

    defend_result = arcane_warrior.defend(2)
    print(f"Defense result: {defend_result}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell("Fireball", [enemy])
    print(f"Spell cast: {spell_result}")

    mana_result = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
