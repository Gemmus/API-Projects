import requests
import random


def riddle_generator():
    url = "https://riddles-api.vercel.app/random"
    response = requests.get(url).json()
    riddle = response['riddle']
    answer = response['answer']
    return riddle, answer


first_question = input("What is your name?  ")
second_question = input("What is your quest?  ")
third_question = random.randint(0, 1)
if third_question == 0:
    ask = input("What is your favorite color?  ").lower()
    if ask != 'blue':
        print("Right. Off you go.")
    else:
        is_blue_really = random.randint(0, 1)
        if is_blue_really == 0:
            print("Right. Off you go.")
        else:
            print(f'{first_question}: "Blue. No yel-- Auuuuuuuugh!"')
else:
    q, a = riddle_generator()
    ask = input(f'{q}  ').lower()
    if ask == a.lower():
        print("Right. Off you go.")
    else:
        print(f'{first_question}: "Auuuuughh!')
        print(f'({a})')


