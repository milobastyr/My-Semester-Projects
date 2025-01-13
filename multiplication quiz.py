#Milo Bastyr
#1/9/2025
#Init
import random
import time
score = 0
#Main
score=score+1

print("Welcome to Multiplication Quiz")
input("Are you ready? yes or no:")
num_questions = int(input("How many questions would you like in the quiz? "))
difficulty = input("Select a difficulty level (easy, medium, hard): ").lower()
if difficulty == "easy":
    max_num = 10
elif difficulty == "medium":
    max_num = 20
elif difficulty == "hard":
    max_num = 50
else:
    print("Invalid difficulty level. Defaulting to easy.")
    max_num = 10
start_time = time.time()
for _ in range(num_questions):
    x = random.randint(1, max_num)
    y = random.randint(1, max_num)
    answer = int(input(f"What is {x} * {y}? "))
    if answer == x * y:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
end_time = time.time()
print(f"Your final score is {score} out of {num_questions}.")
print(f"You took {end_time - start_time:.2f} seconds to complete the quiz.")
