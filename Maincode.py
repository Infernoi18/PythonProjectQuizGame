# Python Quiz Game By Kumar Ayush

print("Welcome to the Python Quiz Game By Kumar Ayush!")
print("You will be asked 5 easy science questions.")
print("Each question has 4 options. Choose the correct one by typing the corresponding number.")
print("Let's begin!\n")

questions = [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "H2SO4"],
        "correct_option": 1
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_option": 2
    },
    {
        "question": "What is the speed of light?",
        "options": ["300,000 km/s", "150,000 km/s", "75,000 km/s", "1,000,000 km/s"],
        "correct_option": 1
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "correct_option": 3
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "correct_option": 3
    }
]

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")
    answer = int(input("Your answer (1/2/3/4): "))
    if answer == q["correct_option"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(f"Your final score is: {score} out of {len(questions)}")
print(f"{(score/len(questions))*100}%")
