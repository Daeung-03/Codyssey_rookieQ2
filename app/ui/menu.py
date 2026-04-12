class Menu:
    def show_main_menu(self):
        print("\n=== 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def show_quiz_list(self, quizzes: list):
        if not quizzes:
            print("저장된 퀴즈가 없습니다.")
            return
        print(f"\n총 {len(quizzes)}개의 퀴즈")
        for i, quiz in enumerate(quizzes, start=1):
            print(f"  {i}. {quiz.question}")

    def show_result(self, score: int, total: int):
        print(f"\n최종 점수: {score} / {total}")

    def show_best_score(self, best_score: int):
        print(f"\n역대 최고 점수: {best_score}점")
