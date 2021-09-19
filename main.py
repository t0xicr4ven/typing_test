from tkinter import *
import random

rand_num_for_para = random.randint(1,5)
FONT=('Courier',18)
user_wrds = []
test_text = []
words_used = []
ran_words = []

def set_starting_wrds():
    test_str = ''
    with open('word_list') as file:
        for line in file:
            word = line.splitlines()
            test_text.append(word)
    for i in range(0,27):
        new_wrd = random.choice(test_text)[0]
        ran_words.append(new_wrd)
        test_str = test_str + new_wrd + ' '
    return test_str


def get_word_fm_entry(self):
    word = entry.get()
    user_wrds.append(word)
    entry.delete(0,END)
    test_wrd = ran_words[0]
    words_used.append(test_wrd)
    ran_words.pop(0)
    update_screen()
    check_if_match()


def check_if_match():
    for index, word in enumerate(user_wrds):
        print(f'word typed is:: {word} act word is:: {words_used[index]}')
        word = word.strip()
        if word == words_used[index]:
            user_wrds.pop(0)
            words_used.pop(0)
            print('matched')
        else:
            user_wrds.pop(0)
            words_used.pop(0)
            print('does not match')

def update_screen():
    # get new random word and add to end of list
    # delete what is currently on screen and put new str on screen
    wrd_str = ''
    t.delete(1.0,END)
    new_wrd = random.choice(test_text)[0]
    ran_words.append(new_wrd)
    for word in ran_words:
        wrd_str = wrd_str + word + ' '
    t.insert(INSERT, wrd_str)

def start_test():
    print('start pressed')


def quit_test():
    window.destroy()


starting_string = set_starting_wrds()
window = Tk()
window.title('Typing Speed Test')
t = Text(wrap=WORD)
t.configure(font=FONT)
t.insert(INSERT, starting_string)
entry = Entry(window, width=50, font=FONT)
entry.focus()
start_btn = Button(window, text='Start', command=start_test)
quit_btn = Button(window, text='Quit', command=quit_test)
t.grid(column=0, row=0, padx=10, pady=10)
entry.grid(column=0,row=1, padx=10, pady=10)
start_btn.grid(column=0, row=2, padx=10, pady=10)
quit_btn.grid(column=1, row=2, padx=10, pady=10)
# when space bar is pressed do checks
window.bind("<space>", get_word_fm_entry)

window.mainloop()
