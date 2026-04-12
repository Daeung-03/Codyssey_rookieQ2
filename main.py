from app.models.quiz_game import QuizGame
from app.services.quiz_service import QuizService
from app.services.score_service import ScoreService
from app.ui.menu import Menu
from app.ui.input_handler import InputHandler

game = QuizGame()

def main():
    
    menu = Menu()
    input_handler = InputHandler()
    quiz_service = QuizService(game, menu, input_handler)
    score_service = ScoreService(game, menu)

    while True:
        menu.show_main_menu()
        choice = input_handler.get_menu_choice()

        if choice == 1:
            score, total = quiz_service.play()
            score_service.update_score(score, total)
        elif choice == 2:
            quiz_service.add()
        elif choice == 3:
            quiz_service.list_quizzes()
        elif choice == 4:
            score_service.show()
        elif choice == 5:
            game.save()
            print("종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        game.save()
        print("\n프로그램이 종료되었습니다.")
