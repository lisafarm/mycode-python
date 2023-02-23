'''
Program: Knock-Knock Jokes
Author: Lisa Klinbuayam
Description: The game to tell a random jokes.
Revision:
    00 : Try the prompt and response in direct way
    01 : Add non-sensitive case handling and remove punctuation
    02 : Extract common logic in functions
    03 : Add more jokes
'''

# import function random
import random


# Define function to check if user responded a valid number of jokes ?
def prompt_num_jokes(jokesToTell, totalJokes):
    if jokesToTell <= 0:
        print(f"You need to ask for at least one joke.")
        return False
    if jokesToTell > totalJokes:
        print(f"There is only {totalJokes} available.")
        return False
    else:
        return True


# Define function to check if user responded expected answer
def prompt_response(prompt, responses, suggest):
    if prompt in responses:
        return True
    else:
        print(f'Sorry. The correct response is "{suggest}"')
        print('Try again\n')
        return False


# Create a list of jokes that contain dictionary for each joke
jokes = [
    {'prompt': 'Nana', 'punchline': "Nana ya bizness"},
    {'prompt': 'Utah', 'punchline': "Utah-kin to me?\nha-ha!"},
    {'prompt': 'Wanda', 'punchline': "Wanda hear another knock knock joke?"},
    {'prompt': 'Kent', 'punchline': "Kent you tell by my voice?"},
    {'prompt': 'A herd', 'punchline': "A herd you were home, so I knocked! hehe."},
    {'prompt': 'Omar', 'punchline': "Omar goodness! I'm at the wrong house...\nhuh!"},
    {'prompt': 'Alpaca', 'punchline': "Alpaca the suit case. You starta the car.\nhehe."},
    {'prompt': 'Diploma', 'punchline': "Diploma is here to fix the sink!"},
    {'prompt': 'Dwayne', 'punchline': "Dwayne the bathtub, I'm dwowning!"}
]

# Define punctuation variable
punct = ".,?!' "

# Introduction
print(f'\nReady to tell a knock-knock joke!\n')

# Announce
print(f'There are {len(jokes)} available.')

# Prompt user for how many jokes?
while True:
    njokes = int(input('How many jokes would you like me to tell? '))
    if prompt_num_jokes(njokes, len(jokes)):
        break

print(f'\nReady to tell {njokes} joke{"s" if njokes > 1 else ""}!\n')  # output how of many jokes will be played

# use loop to tell the selected number of jokes
for i in range(njokes):
    random.shuffle(jokes)  # randomized the list of jokes, so they will be different on each play
    currentJoke = jokes.pop(0)  # use pop function to return the first shuffled joke and remove it from the list
    responses = ["who's there", "who is there", "who there", "whos there"]  # create a list of accepted prompt response
    while True:
        print('Knock-knock!')  # announce
        prompt = input().lower().strip(punct)  # prompt and convert to lower case and remove extra/unwanted characters
        if prompt_response(prompt, responses, "Who's there?"):  # condition to check if user answered ~ "Who's there?"
            print(currentJoke['prompt'])  # output joke prompt
            break

    while True:
        prompt = input().lower().strip(punct)  # prompt and convert to lower case and remove extra/unwanted characters
        if prompt_response(prompt, [currentJoke['prompt'].lower() + ' who'], currentJoke['prompt'] + ' who?'):  # condition to check if user answered prompt + who?
            print(f"{currentJoke['punchline']}\n")  # output punchline
            break

print('Thanks for playing!')  # exit the game