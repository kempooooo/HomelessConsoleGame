import random

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.happiness = 100
        self.health = 100
        self.home = "бездомный"

    def get_status(self):
        return f"{self.name}: 💰 {self.money} | 🙂 {self.happiness} | ❤️ {self.health} | 🏠 {self.home}"

    def is_alive(self):
        return self.health > 0 and self.happiness > 0


class Action:
    def __init__(self, name, money=0, happiness=0, health=0):
        self.name = name
        self.money = money
        self.happiness = happiness
        self.health = health

    def perform(self, player: Player):
        player.money += self.money
        player.happiness += self.happiness
        player.health += self.health
        print(f"\n➡ {player.name} выбрал: {self.name}")
        print(f"изменения: "
              f"{'+' if self.money >= 0 else ''}{self.money}💰, "
              f"{'+' if self.happiness >= 0 else ''}{self.happiness}🙂, "
              f"{'+' if self.health >= 0 else ''}{self.health}❤️")


class RandomEvent:
    def __init__(self, name, money=0, happiness=0, health=0, probability=0.07):
        self.name = name
        self.money = money
        self.happiness = happiness
        self.health = health
        self.probability = probability
    
    def trigger(self, player: Player):
        player.money += self.money
        player.happiness += self.happiness
        player.health += self.health
        print(f'Случайное событие {self.name}')
        print(f"изменения: "
              f"{'+' if self.money >= 0 else ''}{self.money}💰, "
              f"{'+' if self.happiness >= 0 else ''}{self.happiness}🙂, "
              f"{'+' if self.health >= 0 else ''}{self.health}❤️")
        



class Game:
    def __init__(self, player: Player, categories: dict):
        self.player = player
        self.categories = categories

    def show_main_menu(self):
        print("\n------------------------------------------------")
        print(self.player.get_status())
        print("--------------------------------------------------")
        for i, cat in enumerate(self.categories.keys(), 1):
            print(f"{i}. {cat}")
        print("0. выйти")

    def choose_category(self, index: int):
        if index == 0:
            return False
        if 1 <= index <= len(self.categories):
            cat_name = list(self.categories.keys())[index - 1]
            self.show_actions(cat_name)
            return True
        else:
            print("некорректный выбор")
            return True

    def show_actions(self, category: str):
        actions = self.categories[category]
        print(f"\n-- {category} --")
        for i, act in enumerate(actions, 1):
            print(f"{i}. {act.name} "
                  f"({act.money:+}💰, {act.happiness:+}🙂, {act.health:+}❤️)")
        print("0. назад")

        choice = int(input("ваш выбор: "))
        if choice == 0:
            return
        if 1 <= choice <= len(actions):
            actions[choice - 1].perform(self.player)
        else:
            print("некорректный выбор")
    
    def get_chance(self, random_events):
        if random.random() < 0.2:
            event = random.choice(random_events)
            event.trigger(self.player)

