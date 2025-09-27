from models import Player, Action, Game

def main():
    player = Player("Бомж")

    categories = {
        "Работа": [
            Action("собирать бутылки", money=20, happiness=-1, health=-1),
            Action("мыть машины", money=50, happiness=-2, health=-2),
            Action("грузчиком", money=100, happiness=-3, health=-5),
        ],
        "Развлечения": [
            Action("пить пиво", money=-20, happiness=5, health=-5),
            Action("играть в автоматы", money=-50, happiness=10, health=-2),
        ],
        "Здоровье": [
            Action("поспать на лавочке", health=10, happiness=2),
            Action("сходить к врачу", money=-30, health=20),
        ]
    }

    game = Game(player, categories)

    while player.is_alive():
        game.show_main_menu()
        choice = int(input("ваш выбор: "))
        if not game.choose_category(choice):
            break

    print("\n игра окончена!")

if __name__ == "__main__":
    main()





