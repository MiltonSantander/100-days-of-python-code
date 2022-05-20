from question_model import QuestionModel
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    new_question = QuestionModel(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
