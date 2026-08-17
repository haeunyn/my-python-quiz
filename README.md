# Python Quiz Game Project

파이썬 기초 문법과 Git 협업 과정을 학습하기 위한 퀴즈 게임 프로젝트입니다.

## 1. 프로젝트 개요
- **개발 언어**: Python 3.10+
- **주요 기술**: OOP(객체지향), JSON 파일 입출력, Git/GitHub 버전 관리
- **저장소 주소**: [https://github.com/haeunyn/my-python-quiz](https://github.com/haeunyn/my-python-quiz)

## 2. 퀴즈 주제 선정 이유
- 기초 문법 복습: 파이썬 및 CS 기초 개념을 재미있게 학습하고 검증할 수 있는 환경 제공
- 확장성 및 데이터 관리: 사용자가 직접 문제를 추가/삭제하고 JSON 파일에 즉시 반영되는 구조를 통해 데이터 영속성과 예외 처리 실습

## 3. 실행 방법
터미널에서 아래 명령어를 입력하여 게임을 실행합니다.
```bash
python main.py
```

## 4. 기능 목록
- **카테고리별 퀴즈 풀기**: Python, CS, 상식 등 카테고리를 선택하거나 전체 문제를 랜덤으로 플레이
- **힌트 기능 & 시간 측정**: 문제당 힌트 사용 시 점수 감점 로직 적용 및 정답 제출 소요 시간 측정
- **동적 문제 관리**: 새로운 퀴즈 추가(질문, 보기, 정답, 카테고리, 힌트) 및 기존 문제 번호별 삭제
- **기록 및 최고 점수 관리**: 누적 점수, 총 플레이 횟수, 최고 점수 및 일자별 플레이 히스토리 기록
- **예외 처리**: KeyboardInterrupt(Ctrl+C), EOFError(Ctrl+D) 발생 시 데이터를 안전하게 저장(state.json)하고 정상 종료

## 5. 파일 구조
```text
.
├── main.py          # Quiz 및 QuizGame 클래스 정의, 게임 실행 및 예외 처리 로직
├── state.json       # 퀴즈 목록, 히스토리, 최고 점수 영속성 저장 파일
├── README.md        # 프로젝트 설명 및 평가 대응 보고서
└── docs/            
    └── screenshots/ # 실행 화면 및 Git 로그 증빙 캡처 이미지
```

## 6. 데이터 파일 설명 (state.json)
- **경로**: 프로젝트 루트 디렉토리 (`./state.json`)
- **역할**: 프로그램 종료 후에도 데이터가 유지되도록 저장하는 데이터베이스 역할
- **필드 구조**:
  - `quizzes`: 퀴즈 목록 (question, options, answer, category, hint 포함)
  - `history`: 게임 기록 (date, score, total_questions 포함)
  - `high_score`: 최고 점수 정보 (score, date)
 
## 7. Git / GitHub 협업 및 버전 관리

### 10개 이상의 커밋 히스토리 관리
- 기능 구현, 버그 수정, 문서 작성 등 작업 단위별로 세분화하여 커밋을 진행했습니다
- git log --oneline --graph 실행 시 10개 이상의 명확한 커밋 메시지 커밋 내역을 확인할 수 있습니다.

### Feature 브랜치 활용 및 병합 (branch & merge)
- 메인 브랜치 작업과 분리하여 feature/play-quiz 브랜치를 생성해 퀴즈 풀기 및 최고 점수 로직을 독립적으로 개발했습니다.
- 개발 완료 후 git checkout main 및 git merge feature/play-quiz 명령을 수행하여 병합 이력을 남겼습니다.

### 원격 저장소 복제 및 동기화 (clone & pull)
- 별도 테스트 폴더(quiz-clone-test)로 git clone을 실행하여 저장소를 복제한 뒤 수정 작업을 진행했습니다.
- 원격 저장소(origin/main)에 푸시한 내역을 기존 작업 폴더에서 git pull을 통해 동기화하여 다중 환경 협업 프로세스를 검증했습니다.

## 8. 실행 화면 스크린샷

### 메인 메뉴 및 게임 실행
![메인 메뉴](./docs/screenshots/play_main.png)

*프로그램 시작 시 나타나는 메인 메뉴와 퀴즈 풀이 시작 화면입니다.*

### 카테고리 선택 및 퀴즈 풀이
![퀴즈 풀이](./docs/screenshots/play_category.png)

*카테고리별 퀴즈 선택 및 힌트 사용 기능을 포함한 실제 게임 진행 화면입니다.*

### Git 커밋 로그 (10개 이상 달성)
![Git 로그](./docs/screenshots/git_log.png)

*기능 단위로 커밋을 진행하여 프로젝트의 히스토리를 관리한 로그입니다.*

## 9. 학습 포인트 및 예외 처리 성과
- **객체지향 프로그래밍(OOP)**: Quiz 및 QuizGame 클래스로 역할을 분리하여 코드 가독성과 유지보수성을 극대화했습니다.
- **비정상 종료 예외 처리**: 사용자가 입력 도중 Ctrl+C나 Ctrl+D를 눌러 프로그램을 강제 종료하더라도 에러 메시지 출력 대신 안내 문구와 함께 save_data()를 호출하도록 처리했습니다.
- **Git CLI 숙달**: add, commit, push, pull, checkout, merge, clone 등 실무 핵심 Git 명령어를 종합적으로 적용했습니다.



