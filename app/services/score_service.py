from datetime import datetime

from app.models.quiz_game import STATE_FILE
from app.repository.storage import Storage


class ScoreService:
    def __init__(self, game, menu):
        self.game = game
        self.menu = menu
        self._storage = Storage(STATE_FILE)

    def get_best_score(self) -> int:
        return self.game.best_score

    def update_score(self, score: int, total: int):
        if total <= 0:
            return

        prev = self.game.best_score
        self.game.update_best_score(score)
        if self.game.best_score > prev:
            self.menu.show_new_best()

        data = self._storage.load()
        history = data.get('score_history', [])
        history.append(
            {
                'played_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_questions': total,
                'score': score,
            }
        )
        data['score_history'] = history
        self._storage.save(data)
        self.game.save()

    def show(self):
        data = self._storage.load()
        history = data.get('score_history', [])
        self.menu.show_best_score(self.game.best_score, history)
