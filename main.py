from Game import Game
from GameEnv import GameEnv
from stable_baselines3 import PPO

import sys


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "-play"
    
    if mode == "--train":
        env = GameEnv()
        model = PPO("MultiInputPolicy", env, verbose=1)
        model.learn(total_timesteps=500000)
        model.save("button_game_model")
        
    elif mode == "--play":
        # load model into Robot, run Game
        game = Game()
        game.run()



def main():
    game = Game()
    game.run()


from GameEnv import GameEnv

env = GameEnv()



if __name__ == '__main__':
    main()