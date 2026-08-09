class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer.strip().upper()[0] == self.correct_answer


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def play(self):
        score = 0
        for q in self.questions:
            print(q.question)
            for answer in q.answers:
                print(answer)
            user_answer = input("your answer: ")
            if q.check_answer(user_answer):
                print("✅ correct")
                score += 1
            else:
                print("❌ Wrong! the correct answer is:", q.correct_answer)
        print("Quiz finished! your score:", score, "out of", len(self.questions))


quiz = Quiz()
q1 = Question("what's the capital of saudi arabia?", ["A) jeddah", "B) riyadh", "C)makkah"], "B")
q2 = Question("5 + 5 = ?", ["A) 8", "B) 7", "C) 10"], "C")

quiz.add_question(q1)
quiz.add_question(q2)

quiz.play()