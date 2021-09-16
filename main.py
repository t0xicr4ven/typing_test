from tkinter import *
import random

rand_num_for_para = random.randint(1,5)


def set_starting_wrds():
    test_text = []
    test_str = ''
    with open('word_list') as file:
        for line in file:
            word = line.splitlines()
            test_text.append(word)

    print(test_text)
    for i in range(0,17):
        new_wrd = random.choice(test_text)[0]
        print(new_wrd)
        test_str = test_str + new_wrd + ' '
    return test_str


starting_string = set_starting_wrds()
window = Tk()
window.title('Typing Speed Test')
t = Text(wrap=WORD)
#canvas = Canvas(width=600, height=600)
#canvas.grid(column=0, row=0)
t.configure(font=('Courier',18))
t.insert(INSERT, starting_string)
t.grid(column=0, row=0, padx=10, pady=10)
#test_text = canvas.create_text(300,200, text=t)
#test_text.grid(column=0, row=0)

window.mainloop()
