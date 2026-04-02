import time

question = []
answer = []
score= 0

question.append("What is the capital of France?")
answer.append("Paris")
question.append("What is the largest planet in our solar system?")
answer.append("Jupiter")
question.append("What is the chemical symbol for water?")
answer.append("H2O")

for i in range(3):
    user_answer = input(question[i] + " ")
    if user_answer.strip().lower() == answer[i].lower():
        print("Correct! Score + 1")
        score += 1
        time.sleep(0.5)
    else:
        print("Incorrect. The correct answer is: " + answer[i])
        time.sleep(0.5)

print(f"Your final score is: {score}/3")