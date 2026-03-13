from Player import Robot
from Player import Human
# from Player import Robot

class Game:


    def __init__(self):
        self.players = []

        self.p1 = Human("YOU")
        self.p2 = Robot("COMPUTER", "button_game_model")
        self.players.append(self.p1)
        self.players.append(self.p2)


    def endRoundCheck(self):
        return any(abs(player.points) >= 10000 for player in self.players)
        

    def run(self):
        print("\n─────────────────────────────────────────────")
        print('''
How to Play: 
- It's YOU against the CPU!
- Your goal is to reach 10k points first by pressing buttons.
- If you reach -10k points, you automatically lose
- You cannot press the same button 2x in a row.
''')
        i = 1
        while all(-10000 < player.points < 10000 for player in self.players):
            print("=================================")
            print(f"ROUND {i} - P1: " + str(self.p1.points) + " | P2: " + str(self.p2.points))
            print("=================================")
            for player in self.players:
                player.take_turn()
                if self.endRoundCheck():
                    break
            i += 1

            max_points = max(player.points for player in self.players)
            for player in self.players:
                if player.points == max_points:
                    winner = player
                    break

        
        print("\n─────────────────────")
        print(f"Game is over.")
        print(f'''FINAL SCORES:
- {self.p1.name}: {self.p1.points}
- {self.p2.name}: {self.p2.points}
              ''')
        print(f"WINNER: {winner.name}")
        print("─────────────────────")
        
        

        
        




