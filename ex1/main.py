from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard, EffectType


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()
    fire_dragon = CreatureCard(
        "Fire Dragon", 5, Rarity.LEGENDARY, 7, 5
    )
    lightning_bolt = SpellCard(
        "Lightning Bolt", 3, Rarity.COMMON, EffectType.DAMAGE
    )
    mana_crystal = ArtifactCard(
        "Mana Crystal", 2, Rarity.RARE, 3, "+1 mana per turn"
    )

    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    deck.shuffle()

    print("\nDrawing and playing cards:\n")

    game_state = {"mana": 10}

    for _ in range(3):
        card = deck.draw_card()
        card_info = card.get_card_info()
        print(f"Drew: {card_info['name']} ({card_info['type']})")
        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
