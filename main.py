import art
from game_data import data
import random

def choice():
    return random.choice(data)

def compare_display(name1):
    name2 = choice()
    while name2['name'] == name1['name']:
        name2 = choice()
    print(f"Compare A: {name1['name']}, a {name1['description']}, from {name1['country']}.")
    print(art.vs)
    print(f"Against B: {name2['name']}, a {name2['description']}, from {name2['country']}.")
    return name2

def check_winner(user_answer, actual_answer):
    if actual_answer == user_answer:
        return True
    else:
        return False

def compare_count(name1, name2):
    if name1['follower_count'] > name2['follower_count']:
        return 'A'
    else:
        return 'B'

def higher_lower(person1):
    person2 = compare_display(person1)
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    actual_answer = compare_count(person1, person2)
    correct = check_winner(user_answer, actual_answer)
    global Score
    if correct:
        Score += 1
        print(art.logo)
        print(f"You're right! Current score: {Score}")
        higher_lower(person2)
    else:
        print(f"Sorry, that's wrong. Final score: {Score}")


Score = 0
person1 = choice()
print(art.logo)
higher_lower(person1)