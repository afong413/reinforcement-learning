from abc import abstractmethod

import random

from .agent import Agent


class Bot(Agent):
    """A reinforcement learning agent."""

    def __init__[O](
        self,
        epsilon: float,
        rewards: dict[O, tuple[float, float]],
        decay_gamma: float,
        learning_rate: float,
    ):  # fmt: skip
        self.epsilon = epsilon
        self.rewards = rewards
        self.decay_gamma = decay_gamma
        self.learning_rate = learning_rate

        self.q_table = {}

        self.states = []

    @abstractmethod
    def hash_state[S](self, state: S) -> int:
        pass

    def distribute_reward[O](self, outcome: O):
        reward = self.rewards[outcome]
        self.epsilon *= reward[1]
        reward = reward[0]

        for state in reversed(self.states):
            q = self.q_table.get(state, 0)
            self.q_table[state] = q + self.learning_rate * (reward - q)
            reward = self.q_table[state] * self.decay_gamma

        self.states = []

    def get_action[S](
        self,
        current_state: S,
        valid_action_states: list[S]
    ) -> S:  # fmt: skip
        random.seed()

        if random.random() < self.epsilon:
            move = random.choice(valid_action_states)
        else:
            q_values = {
                self.q_table.get(self.hash_state(state), -1): state
                for state in valid_action_states
            }

            max_q = max(q_values)

            if (max_q) == -1:
                move = random.choice(valid_action_states)
            else:
                move = q_values[max_q]

        self.states.append(self.hash_state(move))

        return move
