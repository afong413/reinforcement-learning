# reinforcement-learning

## About

This is a simple implementation of the [Q-Learning](https://en.wikipedia.org/wiki/Q-learning) reinforcement learning algorithm. For simple games such as Tic-Tac-Toe, the agent plays against itself, rating and rerating each possible game state as it goes. After many iterations the agent "knows" what the more desireable states are and is able to play effectively. The agent's knowledge can be stored in `.qtable` files for later use.

## Usage

Run `python3 tictactoe.py -h` to get a list of all arguments and flags.

I have also included an example agent save file that was generated using 10M iterations.
