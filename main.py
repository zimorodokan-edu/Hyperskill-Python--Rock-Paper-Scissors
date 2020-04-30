import random

score = 0
figures = ['paper', 'scissors', 'rock']
commands = ['!exit', '!rating']
u_name = input('Enter your name: ')

print(f'Hello, {u_name}')

f = open('rating.txt', 'r')
for line in f:
    n, s = line.split()
    if u_name == n:
        score = int(s)
        break
f.close()

u_figures = input().strip()
if len(u_figures):
    u_figures = u_figures.split(sep=',')
    if len(u_figures) > 2 and len(u_figures) % 2 == 1:
        figures = u_figures
    else:
        print('Number of figures is not odd')


def create_figure_beat_list(lst):
    list_len = len(lst)
    if list_len > 2 and list_len % 2 == 1:
        beat_number = int((list_len - 1) / 2)
        figure_beat = dict()
        for i in range(list_len):
            temp_list = []
            temp_list.extend(lst[i + 1:])
            temp_list.extend(lst[:i])
            figure_beat[lst[i]] = temp_list[:beat_number]
        return figure_beat
    else:
        print('Number of figures is not odd')


figure_beat_dict = create_figure_beat_list(figures)

print("Okay, let's start")

while True:
    u_input = input()
    if u_input not in commands and u_input not in figures:
        print('Invalid input')
        continue

    computer = random.choice(figures)

    if u_input == '!exit':
        print('Bye!')
        break
    elif u_input == '!rating':
        print(f'Your rating: {score}')
    elif u_input == computer:
        score += 50
        print(f'There is a draw ({computer})')
    elif computer in figure_beat_dict[u_input]:
        print(f'Sorry, but computer chose {computer}')
    elif computer not in figure_beat_dict[u_input]:
        score += 100
        print(f'Well done. Computer chose {computer} and failed')
