#e7-3-10簡單猜數字遊戲
import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("猜數字遊戲")
        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = 0
        self.message = "請從1到100間猜一個數"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.guess_button = Button(master, text="猜猜看", command=self.guess_number)
        self.reset_button = Button(master, text="再玩一次", command=self.reset, state=DISABLED)
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True
        else:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
#        except ValueError:
#            return False
    def guess_number(self):
        self.num_guesses += 1
        if self.guess is None:
            self.message = "請從1到100間猜一個數"
        elif self.guess == self.secret_number:
#            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "恭喜! 你在猜%d次後猜對了" % (self.num_guesses)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        elif self.guess < self.secret_number:
            self.message = "太小了!再猜一次!"
        else:
            self.message = "太大了!再猜一次!"
        self.label_text.set(self.message)
    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0
        self.message = "請從1到100間猜一個數"
        self.label_text.set(self.message)
        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)
root = Tk()
my_gui = GuessingGame(root)
root.mainloop()




