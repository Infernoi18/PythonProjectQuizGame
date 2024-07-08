print("Welcome to the Python Quiz Game By Kumar Ayush!")
print("You will be asked 5 easy science questions.")
print("Each question has 4 options. Choose the correct one by typing the corresponding letter.")
print("Let's begin!\n")

questions = [
    {
        "question": "What is the chemical symbol for water?",
        "options": {"a": "H2O", "b": "O2", "c": "CO2", "d": "H2SO4"},
        "correct_option": "a"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
        "correct_option": "b"
    },
    {
        "question": "What is the speed of light?",
        "options": {"a": "300,000 km/s", "b": "150,000 km/s", "c": "75,000 km/s", "d": "1,000,000 km/s"},
        "correct_option": "a"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Carbon Dioxide", "d": "Hydrogen"},
        "correct_option": "c"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": {"a": "Gold", "b": "Iron", "c": "Diamond", "d": "Platinum"},
        "correct_option": "c"
    }
]

score = 0
for q in questions:
    print(q["question"])
    for key, option in q["options"].items():
        print(f"{key}. {option}")
    answer = input("Your answer (a/b/c/d): ")
    if answer == q["correct_option"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(f"Your final score is: {score} out of {len(questions)}")
print(f"Percentage:{(score / len(questions)) * 100:.2f}%")
