from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # print(question_data)
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()


# print(question_bank)
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]

        # Q.1: A slug's blood is green. (True/False)?:
        input(f"Q.{self.question_number+1}: {current_question.text} (True/False)")
