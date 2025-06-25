from data import question_data
from random import shuffle

class QuizGame:
    def __init__(self, question_count: int = 5):

        # create question objects in a list to be randomized and called

        questions = []
        for item in question_data:
            questions.append(Question(question = item["text"], answer=item["answer"]))
            shuffle(questions) # Randomize questions
            self.questions = questions

        # stats to keep score:
        self.score = 0
        self.question_count = question_count
        ...

    def run(self):
        x = 0
        while x <= self.question_count:
            question = self.questions.pop()
            print(f"\nQuestion #{x + 1}:")
            question.ask_question()
            if question.assess_answer():
                self.score += 1
            x += 1

        # Game complete - Report Score!
        print("Questions Complete!")
        print(f"Score: {self.score}/{self.question_count} ({round(self.score/self.question_count,2)*100}%)")

class Question:
    def __init__(self, question: str, answer: str):
        self.question = question.capitalize()
        self.correct_answer = answer.lower()
        self.user_answer = ""

    def ask_question(self):
        print(self.question)
        self.user_answer = input("\nTrue or False?\n").lower()

    def assess_answer(self):
        if self.correct_answer == self.user_answer:
            print("Correct!")
            return True
        else:
            print("Incorrect")
            return False

QuizGame().run()