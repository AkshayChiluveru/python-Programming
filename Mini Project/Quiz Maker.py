import random

def read_questions(questions):
    questions = []
    with open(questions, 'r') as file:
        for line in file:
            line = line.strip(questions)
            if line:
                questions, answer = line.split(":")
                questions.append((questions, answer))
    return questions

def generate_quiz(questions, num_questions):
    quiz = random.sample(questions, num_questions)
    return quiz

def grade_quiz(quiz, answer_key):
    score = 0
    total_questions = len(quiz)
    for question, answer in quiz:
        if answer_key.get(question) == answer:
            score += 1
    return score, total_questions

# Read the questions from the file
questions = read_questions("questions.txt")

# Generate a random quiz with 5 questions
quiz = generate_quiz(questions, 5)

# Define the answer key (question:answer)
answer_key = {
    "Question 1": "Answer 1",
    "Question 2": "Answer 2",
    "Question 3": "Answer 3",
    "Question 4": "Answer 4",
    "Question 5": "Answer 5"
}

# Grade the quiz
score, total_questions = grade_quiz(quiz, answer_key)

# Print the results
print(f"Score: {score}/{total_questions}")

