# Quiz questions and their options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) London", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0  # Initialize the score to 0

    # Loop through each question in the quiz
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Get the user's answer
        answer = input("Enter your answer (A, B, C, or D): ").upper()

        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!")
            score += 1  # Increment the score for a correct answer
        else:
            print(f"Wrong! The correct answer was {q['answer']}")

    # Provide feedback on the user's performance
    print(f"\nYou scored {score} out of {len(questions)}.")

    # Additional feedback based on the score
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score > 0:
        print("Good job! But there's room for improvement.")
    else:
        print("Better luck next time!")

# Run the quiz
run_quiz()
