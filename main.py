
import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"Здоровье {self.computer.name}: {self.computer.health}")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"Здоровье {self.player.name}: {self.player.health}")


# Пример запуска игры
if __name__ == "__main__":
    hero1 = Hero("Игрок", health=100, attack_power=30)
    hero2 = Hero("Компьютер", health=100, attack_power=25)
    game = Game(hero1, hero2)
    game.start()
