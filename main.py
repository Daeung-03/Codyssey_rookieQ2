from app.models.quiz_game import QuizGame


def main():
    game = QuizGame()
    game.load()
    game.show_menu()


if __name__ == "__main__":
    main()
