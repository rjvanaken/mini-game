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




class Human(Player):
    def __init__(self, name):
        super().__init__(name)


    def displayMenu(self):
            print(f"\nACTION MENU: {self.name}")
            i = 1
            points = [-1000, -500, 10, 500, 1000]
            for i in range(1, 6):
                if i != self.last_pressed: 
                    print(str(i) + ": " + str(points[i - 1]))
                i += 1


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
                    self.points += 9999
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
                break


class Robot(Player):    
    def __init__(self, name):
        super().__init__(name)


