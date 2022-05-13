from tkinter import *
import random

root = Tk()

root.title('Dobbellen')

root.geometry('400x450')
def roll_dice():
  
    dice_codes = ['\u2680', '\u2681',
                  '\u2682','\u2683',
                  '\u2684','\u2685']
   
    numbers = {'\u2680':1, '\u2681':2,
               '\u2682':3, '\u2683':4,
               '\u2684':5, '\u2685':6}
    
   
    d1 = random.choice(dice_codes)
    d2 = random.choice(dice_codes)
  
    if d1 in numbers.keys():
        d1_number = numbers[d1]
    if d2 in numbers.keys():
        d2_number = numbers[d2] 

    dice1.config(text=d1)
    dice2.config(text=d2)
    
    dice1_number.config(text=d1_number)
    dice2_number.config(text=d2_number)
 
    total_numbers.config(text=f'U rolde dit: {d1_number + d2_number}')

frame = Frame(root)
frame.pack(pady=5)

dice1 = Label(frame, font=('ariel', 150), fg='black')
dice1.grid(row=0, column=0, padx=5)
dice2 = Label(frame, font=('ariel', 150), fg='black')
dice2.grid(row=0, column=1, padx=5)

dice1_number = Label(frame, font=('ariel', 18))
dice1_number.grid(row=1, column=0)
dice2_number = Label(frame, font=('ariel', 18))
dice2_number.grid(row=1, column=1)

button = Button(root, text='Roll dobbel', font=('ariel', 24),
                relief=GROOVE, bg='grey', command=roll_dice)
button.pack(pady=20)

total_numbers = Label(root, text='', font=('ariel', 24))
total_numbers.pack(pady=10)
roll_dice()
root.mainloop()