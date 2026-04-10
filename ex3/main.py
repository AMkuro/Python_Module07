from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}\n")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")
    deck = factory.create_themed_deck(3)
    cards = deck.get("cards", [])
    print(f"Hand: {[c._name + ' (' + str(c._cost) + ')' for c in cards]}\n")

    turn_result = engine.simulate_turn()

    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")

    game_report = engine.get_engine_status()
    print("Game Report:")
    print(game_report)

    msg = "\nAbstract Factory + Strategy Pattern: "
    msg += "Maximum flexibility achieved!"
    print(msg)


if __name__ == "__main__":
    main()
