
questions = {
    "What is the capital of Pakistan?": "islamabad",
    "2 + 2 = ?": "4",
    "Which language is this quiz in?": "python"
}

score = 0

for question, answer in questions.items():
    user = input(question + " ").lower()
    if user == answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was: {answer}")

print(f"\nYour final score: {score}/{len(questions)}")
