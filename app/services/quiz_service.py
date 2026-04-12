DEFAULT_QUIZZES = [
    {
        'question': '파이썬 클래스에서 __init__ 메서드의 역할은?',
        'choices': [
            '클래스를 삭제할 때 호출된다',
            '객체가 생성될 때 속성을 초기화한다',
            '클래스의 이름을 반환한다',
            '메서드를 상속받는다',
        ],
        'answer': 2,
    },
    {
        'question': '메서드 안에서 self가 가리키는 것은?',
        'choices': [
            '클래스 자체',
            '부모 클래스',
            '현재 인스턴스(객체)',
            '모듈 전체',
        ],
        'answer': 3,
    },
    {
        'question': '이 프로젝트에서 Quiz 객체를 올바르게 생성하는 코드는?',
        'choices': [
            'Quiz.new("문제", ["선지"], 1)',
            'new Quiz("문제", ["선지"], 1)',
            'Quiz.create("문제", ["선지"], 1)',
            'Quiz("문제", ["선지"], 1)',
        ],
        'answer': 4,
    },
    {
        'question': '레이어드 아키텍처에서 Storage 클래스가 속하는 레이어는?',
        'choices': [
            'models',
            'services',
            'repository',
            'ui',
        ],
        'answer': 3,
    },
    {
        'question': 'Quiz 클래스의 check_answer() 메서드가 반환하는 타입은?',
        'choices': [
            'int',
            'str',
            'None',
            'bool',
        ],
        'answer': 4,
    },
]


class QuizService:
    def __init__(self, game, menu, input_handler):
        self.game = game
        self.menu = menu
        self.input_handler = input_handler
        self._init_defaults()

    def _init_defaults(self):
        if not self.game.quizzes:
            for q in DEFAULT_QUIZZES:
                self.game.add_quiz(q['question'], q['choices'], q['answer'])
            self.game.save()

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
        self.game.update_best_score(score)
        self.game.save()
        return score

    def add(self):
        data = self.input_handler.get_quiz_input()
        self.game.add_quiz(data['question'], data['choices'], data['answer'])
        self.game.save()
        self.menu.show_quiz_added()

    def list_quizzes(self):
        self.menu.show_quiz_list(self.game.quizzes)
