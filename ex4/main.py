from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity=Rarity.LEGENDARY,
        attack=7,
        health=5,
    )
    dragon_id = platform.register_card(fire_dragon)

    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity=Rarity.RARE,
        attack=6,
        health=4,
        base_rating=1150,
    )
    wizard_id = platform.register_card(ice_wizard)

    fire_rank_info = fire_dragon.get_rank_info()
    ice_rank_info = ice_wizard.get_rank_info()

    print(f"{fire_dragon.name} (ID: {dragon_id}):")
    interfaces = TournamentCard.__bases__
    interfaces_display = "[" + ", ".join(c.__name__ for c in interfaces) + "]"
    print(f"- Interfaces: {interfaces_display}")
    print(f"- Rating: {fire_rank_info['rating']}")
    print(f"- Record: {fire_rank_info['record']}\n")

    print(f"{ice_wizard.name} (ID: {wizard_id}):")
    print(f"- Interfaces: {interfaces_display}")
    print(f"- Rating: {ice_rank_info['rating']}")
    print(f"- Record: {ice_rank_info['record']}\n")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for rank, (_, name, rating, record) in enumerate(leaderboard, 1):
        print(f"{rank}. {name} - Rating: {rating} ({record})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
