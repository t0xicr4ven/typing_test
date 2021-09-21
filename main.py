from tkinter import *
import random


rand_num_for_para = random.randint(1,5)
FONT=('Courier',28)
BTN_FONT=('Courier', 18)
word_list = []
ran_words = []
cpm = 0
ccpm = 0

# put test words into list
with open('word_list') as file:
    for line in file:
        word = line.splitlines()
        word_list.append(word)


def start_string():
# pick random words from list and put into string    
    global ran_words
    ran_words = []
    testing_str = ''
    for i in range(0,30):
        wrd = random.choice(word_list)[0]
        ran_words.append(wrd)
        testing_str = testing_str + wrd + ' '
    return testing_str


def check_if_match(self):
    # get word typed, strip space from it
    # check if len is > 0 if so check it against word on screen
    # update cpm and if word matches update wpm
    # matched or not remove word from screen then call update screen
    global cpm, ccpm
    wrd_typed = entry.get()
    wrd_typed = wrd_typed.strip()
    wrd_len=len(wrd_typed)
    if wrd_len > 0:
        entry.delete(0,END)
        cpm += len(ran_words[0])
        cpm_lbl.configure(text=f'CPM:{cpm}')
        if wrd_typed == ran_words[0]:
            ccpm += len(ran_words[0])
            wpm_lbl.configure(text=f'WPM:{ccpm//5}')
            ran_words.pop(0)
            update_screen()
        else:
            ran_words.pop(0)
            update_screen()


def update_screen():
    # get new random word and add to end of list
    # delete what is currently on screen and put new str on screen
    wrd_str = ''
    t.delete(1.0,END)
    new_wrd = random.choice(word_list)[0]
    ran_words.append(new_wrd)
    for word in ran_words:
        wrd_str = wrd_str + word + ' '
    t.insert(INSERT, wrd_str)


def start_test(self):
    # reset cpm ccpm, and their lbls,  delete anything in the entry box
    # re focus to then entry box
    # restart timer
    global cpm, ccpm
    entry.delete(0,END)
    entry.focus()
    entry.config(state='normal')
    window.after(60000, test_finised)
    cpm = 0
    ccpm = 0
    cpm_lbl.configure(text=f'CPM: {cpm}')
    wpm_lbl.configure(text=f'WPM: {ccpm//5}')
    t.delete(1.0, END)
    t.insert(INSERT, start_string())
    t.configure(font=FONT)


def test_finised():
    # delete anytning in entry
    # remove testing words from screen and replace with users WPM
    entry.delete(0,END)
    entry.config(state='disabled')
    t.delete(1.0, END)
    t.insert(INSERT, f'Test complete your WPM is {ccpm//5}')


def quit_test():
    window.destroy()


window = Tk()
window.title('Typing Speed Test')
t = Text(wrap=WORD)
t.configure(font=FONT)
t.insert(INSERT, 'PRESS START TO BEGIN TEST')
entry = Entry(window, width=50, font=FONT)
entry.focus()

start_btn = Button(window, text='Start(Left Shift)', command=start_test,
        font=BTN_FONT)
quit_btn = Button(window, text='Quit', command=quit_test,font=BTN_FONT)
cpm_lbl = Label(window, text=f'CPM: {cpm}',font=FONT)
wpm_lbl = Label(window, text=f'WPM: {ccpm//5}',font=FONT)
# grid placement
cpm_lbl.grid(column=0, row=0, padx=10, pady=10)
wpm_lbl.grid(column=1, row=0, padx=10, pady=10)
t.grid(column=0, columnspan=2, row=1, padx=10, pady=10)
entry.grid(column=0, columnspan=2, row=2, padx=10, pady=10)
start_btn.grid(column=0, row=3, padx=10, pady=10)
quit_btn.grid(column=1, row=3, padx=10, pady=10)
# when space bar is pressed do checks
window.bind("<space>", check_if_match)
window.bind('<Shift_L>', start_test)

window.mainloop()
