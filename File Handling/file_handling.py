# 0157CY221126
# Shiksha Jaiswal

from random import sample
from datetime import datetime

# Function to load users from file
def load_users():
    users = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user, password = line.strip().split(':')
                users[user] = password
    except FileNotFoundError:
        open('users.txt', 'w').close()  # Create file if it doesn't exist
    return users

# Function to save new user to file
def save_result(user_id, topic, score):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('results.txt', 'a') as file:
        file.write(f"{user_id}:{topic}:{score}/5:{timestamp}\n")

# Function to load questions from file
def load_questions(topic):
    questions = []
    try:
        with open(f'{topic}.txt', 'r') as file:
            while True:
                q = file.readline().strip()
                if not q:
                    break
                options = [file.readline().strip() for _ in range(4)]
                ans = file.readline().strip()
                questions.append({"q": q, "options": options, "ans": ans})
    except FileNotFoundError:
        print(f"Error: {topic} questions file not found.")
    return questions

# Function to check password strength
def pswd_check(password):
    lower = 0; upper = 0; digit = 0; special = 0
    length = len(password)
    
    for s in password:
        if s.isalpha():
            if s.isupper():
                upper += 1
            elif s.islower():
                lower += 1
        elif s.isdigit():
            digit += 1
        else:
            if s in ['@', '#', '%']:  # Acceptable special characters
                special += 1

    if length > 8 and length < 20 and digit and lower and upper and special:
        return True
    else:
        return False

# Function to handle user registration
def register(users):
    print("Register")
    while True:
        user_id = input("Create a Username: ")
        if user_id in users:
            print("User already exists! You need to Login")
            return
        password = input("Create your Password: ")
        if pswd_check(password):
            users[user_id] = password
            load_users(user_id, password)  # Save to file
            print("User Registered Successfully!")
            main(users)
            break
        else:
            print("Password Not Strong! Make a strong Password")

# Function to handle user login
def login(users):
    print("Login")
    user_id = input("Enter your User ID: ")
    if user_id not in users:
        print("User not Registered")
        return None
    password = input("Enter your Password: ")
    if users[user_id] == password:
        print("You have Logged In!")
        return user_id
    else:
        print("Incorrect Password")
        return None

# Function to save quiz result with timestamp
def save_result(user_id, topic, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('results.txt', 'a') as file:
        file.write(f"{user_id}:{topic}:{score}/5:{timestamp}\n")

# Function to display all results of a user
def display_results(user_id):
    try:
        with open('results.txt', 'r') as file:
            print(f"\nResults for {user_id}:")
            found = False
            for line in file:
                
                parts = line.strip().split(':', 3)
                
                if len(parts) == 4:
                    user, topic, score, timestamp = parts
                    if user == user_id:
                        found = True
                        print(f"Topic: {topic}, Score: {score}, Date & Time: {timestamp}")
            
            if not found:
                print("No results found for this user.")
    except FileNotFoundError:
        print("No results found yet.")


# Function to choose the topic
def choose_topic(user_id):
    while True:
        print("\n1. Take a Quiz")
        print("2. Display Results")
        print("3. Logout")
        choice = input("Choose an option: ")
        
        if choice == '1':
            topic = input("Choose the topic for the Quiz - 1.Python  2.HTML  3.C++: ")
            if topic == '1':
                take_quiz('py', user_id)
            elif topic == '2':
                take_quiz('html', user_id)
            elif topic == '3':
                take_quiz('cpp', user_id)
            else:
                print("Invalid Option Chosen.")
        elif choice == '2':
            display_results(user_id)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid Option. Please try again.")


# Function to handle the quiz
def take_quiz(topic, user_id):
    questions = load_questions(topic)
    if not questions:
        return
    
    print(f"{topic.upper()} Quiz")
    selected_questions = sample(questions, 5)
    score = 0
    
    for i, q in enumerate(selected_questions):
        print(f"\nQ{i+1}. {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"{j+1}. {opt}")
        answer = input("Enter the option number: ")
        correct_option = q['options'].index(q['ans']) + 1
        
        if answer == str(correct_option):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct Answer: {correct_option}. {q['ans']}")
    
    # Save the result to the file
    save_result(user_id, topic, score)
    
    print(f"\nYour score: {score}/5")
    retry = input("Do you want to take the quiz again? \n1. Yes \n2. No\n")
    if retry == '1':
        choose_topic(user_id)


# Main function
def main(users):
    print("QUIZ")
    while True:
        choice = input("1. Login \n2. Register \n3. Exit\n")
        if choice == '1':
            if login(users):
                user_id = users  # Get user ID after successful login
                choose_topic(user_id)  # Pass user ID to choose_topic
        elif choice == '2':
            register(users)
        elif choice == '3':
            break
        else:
            print("Invalid Input")


# Load users from file and start the program
users = load_users()
main(users)
