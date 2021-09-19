from tkinter import *
import random

rand_num_for_para = random.randint(1,5)
FONT=('Courier',18)
word_user_entered = []
test_text = []
def set_starting_wrds():
    test_str = ''
    with open('word_list') as file:
        for line in file:
            word = line.splitlines()
            test_text.append(word)
    for i in range(0,27):
        new_wrd = random.choice(test_text)[0]
        test_str = test_str + new_wrd + ' '
    return test_str


def get_word_fm_entry(self):
    word = entry.get()
    print(f'key pressed and getting word {word}')
    word_user_entered.append(word)
    print(word_user_entered)
    entry.delete(0,END)

starting_string = set_starting_wrds()
window = Tk()
window.title('Typing Speed Test')
t = Text(wrap=WORD)
t.configure(font=FONT)
t.insert(INSERT, starting_string)
t.grid(column=0, row=0, padx=10, pady=10)
entry = Entry(window, width=50, font=FONT)
entry.grid(column=0,row=1, rowspan=2, padx=10, pady=10)
entry.focus()

window.bind("<space>", get_word_fm_entry)

window.mainloop()
