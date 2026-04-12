class QuizService:
    def __init__(self, game, menu, input_handler):
        self.game = game
        self.menu = menu
        self.input_handler = input_handler

    def play(self) -> int:
        if not self.game.quizzes:
            self.menu.show_no_quizzes()
            return 0

        score = 0
        for quiz in self.game.quizzes:
            quiz.display()
            answer = self.input_handler.get_answer()
            if quiz.check_answer(answer):
                self.menu.show_correct()
                score += 1
            else:
                self.menu.show_wrong(quiz.answer)

        self.menu.show_result(score, len(self.game.quizzes))
        self.game.update_max_score(score)
        self.game.save()
        return score

    def add(self):
        data = self.input_handler.get_quiz_input()
        self.game.add_quiz(data['question'], data['choices'], data['answer'])
        self.game.save()
        self.menu.show_quiz_added()

    def list_quizzes(self):
        self.menu.show_quiz_list(self.game.quizzes)
