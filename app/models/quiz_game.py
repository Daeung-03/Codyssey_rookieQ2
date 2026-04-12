from app.models.quiz import Quiz
from app.repository.storage import Storage

STATE_FILE = 'state.json'


class QuizGame:
    def __init__(self):
        self.max_score: int = 0
        self.quizzes: list = []
        self._storage = Storage(STATE_FILE)
        self.load()

    def add_quiz(self, question: str, choices: list, answer: int):
        self.quizzes.append(Quiz(question, choices, answer))

    def update_max_score(self, score: int):
        if score > self.max_score:
            self.max_score = score

    def save(self):
        data = {
            'max_score': self.max_score,
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
        self.max_score = data.get('max_score', 0)
        self.quizzes = [
            Quiz(q['question'], q['choices'], q['answer'])
            for q in data.get('quizzes', [])
        ]
