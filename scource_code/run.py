from utils import *
from utils.env import ConnectFour
from utils.minimax_agent import MinimaxAgent

agent = MinimaxAgent()
env = ConnectFour(ai_on=True, agent=agent, n_cols=7, n_rows=6)

if __name__ == "__main__":
    observation = env.reset()

    while True: 
        env.render()

        action = env.get_action(observation)

        if action in get_valid_locations(env.board):
            observation = env.step(action)
