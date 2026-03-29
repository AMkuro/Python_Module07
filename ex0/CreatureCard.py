from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
