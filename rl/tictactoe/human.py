from ..agent import Agent


class Human(Agent):
    """
    An agent that allows the user to select its moves.
    """

    def __init__(self, symbol: str, name: str):
        self.symbol = symbol
        self.name = name

    def get_action(
        self,
        current_state: list[str | None],
        valid_action_states: list[list[str | None]],
        display=True,
    ) -> list[str | None]:
        """
        Asks the user what move they want to make. And if they type in
        something wrong it asks them again ...and again ...and again.
        Don't set `display` to `false`. That would just make it annoying
        for the user. It's just there for compatability.
        """
        action_state = None
        user_in = input("Please input your move: " if display else "").strip()
        if user_in in list("123456789"):
            action_state = current_state.copy()
            action_state[int(user_in) - 1] = self.symbol
        while action_state not in valid_action_states:
            if user_in != "":
                print(f"{user_in} is not a valid move.")
            user_in = input("Please input your move: " if display else "")
            if user_in in list("123456789"):
                action_state = current_state.copy()
                action_state[int(user_in) - 1] = self.symbol

        return action_state
