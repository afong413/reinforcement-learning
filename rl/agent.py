from abc import abstractmethod


class Agent:
    """A generic agent."""

    @abstractmethod
    def get_action[S](
        self, current_state: S,
        valid_action_states: list[S]
    ) -> S:  # fmt: skip
        pass
