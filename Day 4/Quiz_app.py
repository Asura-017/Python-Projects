import random

# List of dictionaries to store the questions and possible answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "J.K. Rowling", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Au", "Pb", "Fe"],
        "answer": "Au"
    },
    {   
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Thailand"],
        "answer": "Japan"
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": "Blue Whale"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Diamond", "Iron", "Platinum"],
        "answer": "Diamond"
    },
]

def run_quiz():
    # Shuffle the questions to randomize the order each time
    random.shuffle(questions)

    score = 0  # Variable to track the score
    
    # Loop through each question
    for idx, question in enumerate(questions):
        print(f"Q{idx+1}: {question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
        
        # Get the user's answer
        user_answer = input("Your answer (type the number): ")
        
        # Check if the user's answer is correct
        try:
            user_answer = int(user_answer)
            if question['options'][user_answer - 1] == question['answer']:
                score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer was {question['answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to your choice.\n")

    # Display the final score
    print(f"Your final score is: {score}/{len(questions)}")

# Run the quiz
run_quiz()
