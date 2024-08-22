from abc import abstractmethod

from .agent import Agent
from .bot import Bot


class Environment:
    def __init__[S](self, starting_state: S):
        self.starting_state = starting_state

    @abstractmethod
    def get_valid_states[S](self, current_state: S, agent: Agent) -> list[S]:
        pass

    @abstractmethod
    def evaluate_state[S](self, state: S) -> int | None:
        pass

    def game(self, agents: list[Agent], reward=False):
        state = self.starting_state

        agent_turn = 0

        outcome = self.evaluate_state(state)

        while outcome is None:
            valid_states = self.get_valid_states(state, agent[agent_turn])

            state = agents[agent_turn].get_action(state, valid_states)

            agent_turn = (agent_turn + 1) % len(agents)

            outcome = self.evaluate_state(state)

        if reward:
            for agent in agents:
                if isinstance(agent, Bot):
                    agent.distribute_reward(outcome)

        return outcome
