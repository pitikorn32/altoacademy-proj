import random
import time


class Player:
    def __init__(self, username) -> None:
        self.username = username
        self.gesture = ["rock", "paper", "scissor"]
        self.result = ""
        self.score = 0

    def get_gesture(self):
        pass

    def get_username(self):
        return self.username

    def get_result(self):
        return self.result

    def get_score(self):
        return self.score

    def increment_score(self, add_score=1):
        self.score += add_score


class Human(Player):
    def __init__(self, username) -> None:
        super().__init__(username)

    def get_gesture(self):
        self.result = input(f"{self.username} gesture (rock, paper, scissor): ")
        assert self.result in self.gesture, "Not Valid"


class Bot(Player):
    def __init__(self, username) -> None:
        super().__init__(username)

    def get_gesture(self):
        self.result = random.choice(self.gesture)
        print(f"{self.username} gesture : {self.result}")


class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2

        self.rules = {"rock": ["scissor"], "scissor": ["paper"], "paper": ["rock"]}

        self.round = 1

    def play(self):
        player1_username = self.player1.get_username()
        player2_username = self.player2.get_username()

        print(f"{player1_username} VS {player2_username}")
        print(f"Round {self.round}")

        self.player1.get_gesture()
        self.player2.get_gesture()

        player1_result = self.player1.get_result()
        player2_result = self.player2.get_result()

        if player1_result == player2_result:
            pass
        else:
            if player2_result in self.rules[player1_result]:
                self.player1.increment_score(1)
            else:
                self.player2.increment_score(1)

        print(
            f"score {player1_username}: {self.player1.get_score()}, {player2_username}: {self.player2.get_score()}"
        )
        print(f"-----------------------------")

        self.round += 1


if __name__ == "__main__":
    # user = Human(username="Pie")
    bot = Bot(username="Bot")
    bot2 = Bot(username="Bot2")

    game = Game(player1=bot, player2=bot2)

    while True:
        game.play()
        time.sleep(1)
