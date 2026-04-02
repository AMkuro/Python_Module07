from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self._durability: int = durability
        self._effect: str = effect

    def play(self, game_state: dict) -> dict:
        result_dict = super().play(game_state)
        result_dict["effect"] = self._effect
        return result_dict

    def activate_ability(self) -> dict:
        pass
