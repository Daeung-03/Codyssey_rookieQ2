class InputHandler:
    def _get_string(self, prompt: str) -> str:
        while True:
            raw = input(prompt).strip()
            if raw:
                return raw
            print("입력값이 비어있습니다. 다시 입력해주세요.")

    def _get_int(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("입력값이 비어있습니다. 숫자를 입력해주세요.")
                continue
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
        question = self._get_string("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choices.append(self._get_string(f"선택지 {i}: "))
        answer = self._get_int("정답 번호 (1~4): ", 1, 4)
        return {'question': question, 'choices': choices, 'answer': answer}
