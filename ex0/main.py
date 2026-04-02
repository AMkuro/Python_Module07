from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 1, "Common", 2, 3)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    available_mana: int = 6
    print(f"Playing Fire Dragon with {available_mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    try:
        play_result = fire_dragon.play({"mana": available_mana})
        print(f"Play result: {play_result}")
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target(goblin_warrior)
    print(f"Attack result: {attack_result}\n")

    insufficient_mana: int = 3
    print(f"Testing insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(insufficient_mana)}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
