import gymnasium as gym
from gymnasium import spaces
import numpy as np

from Player import Human

class GameEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.player = Human("Robot")
        self.ACTION_MAP = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        self.POINTS_MAP = {1: -1000, 2: -500, 3: 10, 4: 500, 5: 1000}

        self.action_space = spaces.Discrete(5)

        self.observation_space = spaces.Dict({
            "my_points":    spaces.Box(low=-11000, high=11000, shape=(1,), dtype=np.int32),
            "last_pressed": spaces.Discrete(6),
        })


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        self.player.points = 0
        self.player.last_pressed = 0
        self.player.turn_penalty = 0
        
        obs = {

            "my_points": np.array([0]),
            "last_pressed": 0 
        }
        return obs, {}
    

    def step(self, action):
        
        mod_action = self.ACTION_MAP[action]

        # reward
        if mod_action == self.player.last_pressed:
            reward = -9999
        else:
            self.player.points += self.POINTS_MAP[mod_action]
            reward = 1 - self.player.turn_penalty

        self.player.turn_penalty += 1

        self.player.last_pressed = mod_action

        # obs
        obs = {
            "my_points": np.array([self.player.points]),
            "last_pressed": self.player.last_pressed
        }     

        terminated = abs(self.player.points) >= 10000 # True if agent reached a terminal state
        truncated = False   # True if episode hit a time limit
        info = {"turn_penalty": self.player.turn_penalty}

        return obs, reward, terminated, truncated, info