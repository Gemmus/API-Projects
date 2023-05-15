import requests

right_answers = 0


def riddle_generator():
    url = "https://riddles-api.vercel.app/random"
    response = requests.get(url).json()
    riddle = response['riddle']
    answer = response['answer']
    return riddle, answer


name = input("Hello! Who are you?  ")
start = input(f"{name}, shall we play a riddle game of five?[yes/no]  ").lower()
while start != 'yes':
    start = input(f"{name}, are you now ready to play a riddle game of five?[yes/no]  ").lower()
else:
    for i in range(4):
        q, a = riddle_generator()
        riddle = input(f"\n{q}  ").lower()
        if riddle == a.lower():
            print('Right answer')
            right_answers += 1
        else:
            print(f'Wrong answer. ({a})')
    print(f'Game ended. You had answered: {right_answers}/5.')
