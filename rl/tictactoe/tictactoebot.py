import random

from ..bot import Bot


class TicTacToeBot(Bot):
    def __init__(
        self,
        symbol: str,
        name: str,
        epsilon: float,
        rewards: dict[str, float],
        decay_gamma: float,
        learning_rate: float,
    ):
        self.symbol = symbol
        self.name = name

        super().__init__(epsilon, rewards, decay_gamma, learning_rate)

    def hash_state(self, state: list[str | None]):
        hash = 0

        for i in range(len(state)):
            if state[i] is None:
                hash += 3**i
            elif state[i] == self.symbol:
                hash += 2 * 3**i

        return str(hash)  # Because of stupid JSON

    def get_action(
        self,
        current_state: list[str | None],
        valid_action_states: list[list[str | None]],
        display=True,
    ) -> list[str | None]:
        random.seed()

        if random.random() < self.epsilon:
            move = random.choice(valid_action_states)
            if display:
                print("Randomly selecting move...")
        else:
            q_values = {
                self.q_table.get(self.hash_state(state), -1): state
                for state in valid_action_states
            }

            max_q = max(q_values)

            if (max_q) == -1:
                move = random.choice(valid_action_states)
                if display:
                    print("Randomly selecting move...")
            else:
                move = q_values[max_q]
                if display:
                    print(f"Selecting move with Q-value {max_q}.")

        self.states.append(self.hash_state(move))

        return move
