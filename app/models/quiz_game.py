from app.models.quiz import Quiz
from app.repository.storage import Storage

STATE_FILE = 'state.json'


class QuizGame:
    def __init__(self):
        self.best_score: int = 0
        self.quizzes: list = []
        self._storage = Storage(STATE_FILE)
        self.load()

    def add_quiz(self, question: str, choices: list, answer: int):
        self.quizzes.append(Quiz(question, choices, answer))

    def update_best_score(self, score: int):
        if score > self.best_score:
            self.best_score = score

    def save(self):
        data = {
            'best_score': self.best_score,
            'quizzes': [
                {
                    'question': q.question,
                    'choices': q.choices,
                    'answer': q.answer
                }
                for q in self.quizzes
            ]
        }
        try:
            self._storage.save(data)
        except OSError as e:
            print(f"저장 실패: {e}")

    def load(self):
        data = self._storage.load()
        if not data:
            return
        self.best_score = data.get('best_score', 0)
        self.quizzes = [
            Quiz(q['question'], q['choices'], q['answer'])
            for q in data.get('quizzes', [])
        ]
