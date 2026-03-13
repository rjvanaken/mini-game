from stable_baselines3 import PPO
import numpy as np

class Player:
    def __init__(self, name):
        self.points = 0
        self.last_pressed = None
        self.name = name
        self.valid_actions = [1, 2, 3, 4, 5]
        self.turn_penalty = 0


    def setValidActions(self):
        self.valid_actions = [1, 2, 3, 4, 5]
        for num in self.valid_actions:
            if num == self.last_pressed:
                self.valid_actions.remove(num)
                return


    def displayMenu(self):
            print(f"\nACTION MENU: {self.name}")
            i = 1
            points = [-1000, -500, 10, 500, 1000]
            for i in range(1, 6):
                if i != self.last_pressed: 
                    print(str(i) + ": " + str(points[i - 1]))
                i += 1


class Human(Player):
    def __init__(self, name):
        super().__init__(name)




    def take_turn(self):

        while True:

            self.displayMenu()
            action = input("\nENTER CHOICE: ")
            try:
                if int(action) == self.last_pressed:
                    print("Invalid choice, try again.")
                    success = False
                elif action == "1":
                    self.points -= 1000
                    self.last_pressed = 1
                    success = True
                elif action == "2":
                    self.points -= 500
                    self.last_pressed = 2
                    success = True
                elif action == "3":
                    self.points += 10
                    self.last_pressed = 3
                    success = True
                elif action == "4":
                    self.points += 500
                    self.last_pressed = 4
                    success = True
                elif action == "5":
                    self.points += 1000
                    self.last_pressed = 5
                    success = True
                else:
                    print("Invalid choice, try again.")
                    
            except Exception as e:
                print(f"Action failed: {e}")

            if success:
                print(f"\n{self.name} chose: {action}")
                break


class Robot(Player):    
    def __init__(self, name, model_path):
        super().__init__(name)
        self.model = PPO.load(model_path)

        self.ACTION_MAP = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        self.POINTS_MAP = {1: -1000, 2: -500, 3: 10, 4: 1000, 5: 2000}

    
    def take_turn(self):

        # self.displayMenu()
        obs = {
            "my_points": np.array([self.points]),
            "last_pressed": self.last_pressed or 0
        }

        action, _ = self.model.predict(obs)

        mod_action = self.ACTION_MAP[int(action)]

        if mod_action != self.last_pressed:
            self.points += self.POINTS_MAP[mod_action]
            
        self.last_pressed = mod_action

        print(f"{self.name} chose: {mod_action}")


