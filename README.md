# Codyssey_rookieQ2
2026 코디세이 AI 올인원 교육과정 입학연수과정 문제 2번

---

## 프로젝트 개요

> 퀴즈 게임 프로그램을 작성하여 Python 기초 문법, 객체지향 설계, JSON 데이터 영속성, Git 사용법을 익힌다.
> 터미널에서 동작하며 퀴즈 풀기, 추가, 목록, 점수확인 기능을 제공한다.

---

## 퀴즈 주제 선정 이유

> 작성전

---

## 개발 환경
| 항목 | 내용 |
|------|------|
| OS | macOS (Darwin)|
| Git | `git version 2.50.1`|
| python | `Python version 3.14.2` |

---

## 실습 계획

### 1. 퀴즈 게임 개발
1. 객체지향 및 레이어드 아키텍쳐를 도입하여 구조를 셋팅합니다. []

  1.1 핵심은 모델과 서비스 계층을 구분하는 것입니다.

  1.2 model(클래스 정의) -> repository(json I/O) -> services(게임 로직, 저장 로직) -> ui(터미널 입출력)

  1.3 레이어에 맞게 디렉토리 구조 설계 []

2. 독립된 패키치 설치공간을 제공하는 파이썬의 가상환경을 사용합니다. 또한 사용된 라이브러기 발생한다면 requirments.txt로 저장합니다. []

  2.1 venv 활성화, 파이썬 버전 선택 []

  2.2 pip3 freeze 사용하여 requirments.txt 생성 []

3. .gitignore를 작성합니다. 기초는 gitignore.io에서 가져옵니다. []

4. 클래스 작성 []

  4.1 quiz 클래스 구현(속성: 문제, 선지, 정답 / 메소드: 퀴즈 출력, 정답 확인)

  4.2 quiz_game 클래스 구현(속성: 최대 정답 수, 퀴즈 목록(List) / 메소드: 메뉴 표시, 퀴즈 풀기, 퀴즈 추가, 목록 보기, 점수 확인, 파일 저장/불러오기)

5. 서비스 구현 []

  5.1 기본 퀴즈 데이터 추가, 풀기 기능 구현 []

  5.2 퀴즈 목록 보기, 추가 기능 구현 []

  5.3 점수 저장 및 확인 기능 구현 []

  5.4 Json 입출력 구현 []

  5.5 quiz_game 클래스 구조 통합 []
  

### 2. Git 브랜치 전략 및 계획
1. Git 푸시 전략 & 레포 관리 전략
브랜치 전략 (기능별 브랜치)

main
├── feat/quiz-class        → Quiz 클래스 구현
├── feat/quiz_game-class   → quiz_game 클래스 구현
├── feat/play-quiz         → 퀴즈 풀기 기능 (과제 요구 브랜치 포함)
├── feat/add-quiz          → 퀴즈 추가 기능
├── feat/file-io           → JSON 저장/불러오기
└── docs/readme            → README.md 완성

커밋 메시지는 type: 설명 형식으로 통일합니다.

type(feat: 기능, 클래스 구현 / fix: 수정 / chore: docs 수정 및 생성, 기타 수정)

state.json은 .gitignore에서 제외 (과제 요구사항이므로 커밋 대상)

clone + pull 실습은 개발 완료 후 별도 디렉터리에서 순서대로 진행

main 브랜치는 항상 동작하는 상태를 유지, 기능 개발은 feat/* 브랜치에서 진행 후 병합
---

### 3. 필수 개념 학습 및 정리
> 실습을 바탕으로 다음 질문에 대한 답을 작성한다.

1. Python 기초

변수와 자료형 (int, str, bool, list, dict)

조건문 (if / elif / else)

반복문 (for vs while 차이 및 선택 기준)

함수 정의, 매개변수, 반환값

2. 객체지향 프로그래밍

클래스와 객체 개념, 왜 쓰는가

__init__과 self의 역할

속성(attribute)과 메서드(method)

3. 파일 입출력 & 예외 처리

파일 open / read / write 기본

JSON 형식이란, 왜 데이터 저장에 쓰는가

try / except 오류 처리 패턴

4. Git & GitHub 기초

Git이 왜 필요한가 (버전 관리의 목적)

핵심 명령어: init, add, commit, push, pull, clone, checkout

브랜치 생성 및 병합 (merge)

원격 저장소 활용 (clone, pull 실습)

## 실행 방법

```bash
# 저장소 클론
git clone https://github.com/{username}/quiz-game.git
cd quiz-game

# 실행
python main.py
```

> Python 3.x 이상 필요. 외부 라이브러리 없음 (표준 라이브러리만 사용).

---

## 기능 목록

| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 저장된 퀴즈를 순서대로 출제, 정답/오답 즉시 피드백, 최종 점수 표시 |
| 2 | 퀴즈 추가 | 문제·선택지 4개·정답 번호를 입력받아 저장 |
| 3 | 퀴즈 목록 | 현재 저장된 퀴즈 전체 목록 출력 |
| 4 | 점수 확인 | 역대 최고 점수 조회, 퀴즈 풀기 후 자동 갱신 |
| 5 | 종료 | 현재 상태 저장 후 프로그램 안전 종료 |

---

## 파일 구조

```
quiz-game/
├── main.py                   # 진입점: 레이어 조립 및 실행 루프
├── state.json                # 퀴즈 데이터 + 최고 점수 (런타임 생성)
├── README.md
├── .gitignore
└── app/
    ├── models/
    │   ├── quiz.py           # quiz 클래스 정의
    │   └── quiz_game.py      # quiz_game 클래스 정의
    ├── repository/
    │   └── storage.py        # JSON 저장/불러오기
    ├── services/
    │   ├── quiz_service.py   # 퀴즈 풀기·추가·목록 로직
    │   └── score_service.py  # 점수 비교·갱신 로직
    └── ui/
        ├── menu.py           # 메뉴 출력·화면 렌더링
        └── input_handler.py  # 입력 수집·유효성 검사·예외 처리
```

---

