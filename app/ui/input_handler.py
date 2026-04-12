class InputHandler:
    def _get_int(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            raw = input(prompt).strip()
            if raw.lstrip('-').isdigit():
                value = int(raw)
                if min_val <= value <= max_val:
                    return value
            print(f"{min_val}~{max_val} 사이의 정수를 입력하세요.")

    def get_menu_choice(self) -> int:
        return self._get_int("선택: ", 1, 5)

    def get_answer(self) -> int:
        return self._get_int("정답 번호를 입력하세요: ", 1, 4)

    def get_quiz_input(self) -> dict:
        question = input("문제를 입력하세요: ").strip()
        choices = []
        for i in range(1, 5):
            choices.append(input(f"선택지 {i}: ").strip())
        answer = self._get_int("정답 번호 (1~4): ", 1, 4)
        return {'question': question, 'choices': choices, 'answer': answer}
