import json
import random
import time
import os

# [클래스 1] 개별 퀴즈 정보를 관리하는 클래스
class Question:
    def __init__(self, category, question, options, answer):
        self.category = category
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_input):
        return user_input.strip().upper() == self.answer.upper()

# [클래스 2] 게임의 전체 로직과 상태를 관리하는 클래스
class QuizGame:
    def __init__(self):
        self.questions = self.load_quiz_data()
        self.score = 0
        self.state_file = "state.json"
        self.user_data = self.load_state()

    def load_quiz_data(self):
        # 퀴즈 데이터 (리스트/딕셔너리 구조)
        data = [
            {"cat": "Python", "q": "Python에서 리스트에 요소를 추가하는 함수는?", "opt": ["A. add()", "B. append()", "C. push()", "D. insert()"], "ans": "B"},
            {"cat": "Python", "q": "Python의 창시자는?", "opt": ["A. 제임스 고슬링", "B. 빌 게이츠", "C. 귀도 반 로섬", "D. 스티브 잡스"], "ans": "C"},
            {"cat": "CS", "q": "HTTP의 기본 포트 번호는?", "opt": ["A. 80", "B. 443", "C. 22", "D. 3306"], "ans": "A"},
            {"cat": "CS", "q": "다음 중 운영체제가 아닌 것은?", "opt": ["A. Linux", "B. Windows", "C. Docker", "D. macOS"], "ans": "C"},
            {"cat": "상식", "q": "대한민국의 수도는?", "opt": ["A. 부산", "B. 서울", "C. 인천", "D. 대구"], "ans": "B"}
        ]
        return [Question(d["cat"], d["q"], d["opt"], d["ans"]) for d in data]

    def load_state(self):
        # state.json에서 기존 점수 불러오기 (보너스: 진행 상황 저장)
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"total_score": 0, "games_played": 0}

    def save_state(self):
        # state.json에 결과 저장
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.user_data, f, ensure_ascii=False, indent=4)

    def run(self):
        print("=== 🚀 파이썬 퀴즈 게임에 오신 것을 환영합니다! ===")
        print(f"현재 누적 점수: {self.user_data['total_score']}점")
        
        # 카테고리 선택 (보너스: 카테고리 기능)
        categories = list(set(q.category for q in self.questions))
        print(f"\n선택 가능한 카테고리: {', '.join(categories)}")
        choice = input("도전할 카테고리를 입력하세요 (전체는 Enter): ").strip()
        
        filtered_questions = [q for q in self.questions if not choice or q.category == choice]
        random.shuffle(filtered_questions) # 보너스: 문제 셔플

        current_game_score = 0
        
        for i, q in enumerate(filtered_questions[:3], 1): # 최대 3문제 진행
            print(f"\n[문제 {i}] (카테고리: {q.category})")
            print(f"질문: {q.question}")
            for opt in q.options:
                print(opt)
            
            start_time = time.time() # 보너스: 타이머 시작
            user_ans = input("정답(A/B/C/D)을 입력하세요: ")
            end_time = time.time()
            
            taken = end_time - start_time
            
            # Python 3.10+ match-case 문법 사용
            if q.is_correct(user_ans):
                print(f"✅ 정답입니다! ({taken:.2f}초 소요)")
                current_game_score += 10
            else:
                print(f"❌ 틀렸습니다. 정답은 {q.answer}입니다.")

        # 결과 업데이트
        self.user_data["total_score"] += current_game_score
        self.user_data["games_played"] += 1
        self.save_state()

        print("\n" + "="*30)
        print(f"게임 종료! 이번 판 점수: {current_game_score}")
        print(f"누적 점수: {self.user_data['total_score']}")
        print(f"총 플레이 횟수: {self.user_data['games_played']}")
        print("="*30)

if __name__ == "__main__":
    game = QuizGame()
    game.run()
