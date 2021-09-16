from tkinter import *
import random

rand_num_for_para = random.randint(1,5)
FONT=('Courier',18)

def set_starting_wrds():
    test_text = []
    test_str = ''
    with open('word_list') as file:
        for line in file:
            word = line.splitlines()
            test_text.append(word)
    for i in range(0,17):
        new_wrd = random.choice(test_text)[0]
        test_str = test_str + new_wrd + ' '
    return test_str


starting_string = set_starting_wrds()
window = Tk()
window.title('Typing Speed Test')
t = Text(wrap=WORD)
t.configure(font=FONT)
t.insert(INSERT, starting_string)
t.grid(column=0, row=0, padx=10, pady=10)
entry = Entry(window, width=100, font=FONT)
entry.grid(column=0,row=1, rowspan=2, padx=10, pady=10)

window.mainloop()
