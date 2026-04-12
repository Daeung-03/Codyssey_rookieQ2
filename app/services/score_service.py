class ScoreService:
    def __init__(self, game, menu):
        self.game = game
        self.menu = menu

    def get_best_score(self) -> int:
        return self.game.best_score

    def update_score(self, score: int):
        prev = self.game.best_score
        self.game.update_best_score(score)
        if self.game.best_score > prev:
            self.menu.show_new_best()

    def show(self):
        self.menu.show_best_score(self.game.best_score)
