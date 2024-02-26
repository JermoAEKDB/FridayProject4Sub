import random

quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "In which year did World War II end?": "1945",
    "Who is known as the 'Father of Computer Science'?": "Alan Turing"
}

questions_list = list(quiz_questions.items())
random.shuffle(questions_list)

varCorrectAnswer = 0

for question, correct_answer in questions_list:
    print(question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        varCorrectAnswer += 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}\n")

print(f"Quiz completed. Your score: {varCorrectAnswer}/{len(quiz_questions)}")
