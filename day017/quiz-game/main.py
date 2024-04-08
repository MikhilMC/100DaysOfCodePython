from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
print(quiz.still_has_questions())
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed this quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
