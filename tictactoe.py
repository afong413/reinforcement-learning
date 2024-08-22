import argparse
import json

from rl import *
from rl.tictactoe import *
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Tic-Tac-Toe")

    parser.add_argument(
        "-t", "--training", action="store_true", help="Train the models."
    )

    parser.add_argument(
        "-n",
        "--number",
        default=1000000,
        type=int,
        help="Number of times to train.",
    )

    parser.add_argument(
        "-o", "--order", action="store_true", help="Swap order so goes first."
    )

    parser.add_argument(
        "-f",
        "--file",
        default="agent.q",
        help="Where to store/load the model Q-tables.",
    )

    args = parser.parse_args()

    if args.training:
        agent1 = TicTacToeBot(
            "X",
            "BOT 1",
            0.2,
            {"X": (1, 1.01), "O": (0, 1), False: (0.1, 1)},
            0.9,
            0.2,
        )
        agent2 = TicTacToeBot(
            "O",
            "BOT 2",
            0.2,
            {"X": (0, 1), "O": (1, 1.01), False: (0.1, 1)},
            0.9,
            0.2,
        )

        env = TicTacToeEnv()

        for i in tqdm(range(args.number), desc="Training..."):
            env.game(agent1, agent2, True, False)

        with open(args.file, "w") as f:
            agent1.q_table.update(agent2.q_table)
            json.dump(agent1.q_table, f)
            f.close()

    else:
        if args.order:
            agent1 = Human("X", "Human")
            agent2 = TicTacToeBot(
                "O",
                "Computer",
                0,
                {},
                0,
                0,
            )

            with open(args.file, "r") as f:
                agent2.q_table = json.load(f)
                f.close()
        else:
            agent1 = TicTacToeBot(
                "X",
                "Computer",
                0,
                {},
                0,
                0,
            )
            agent2 = Human("O", "Human")

            with open(args.file, "r") as f:
                agent1.q_table = json.load(f)
                f.close()

        env = TicTacToeEnv()

        env.game(agent1, agent2)
