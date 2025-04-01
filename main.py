#Creating a timer with GUI based on Pomodoro technique. Using TKinter GUI
#From FreedomOutlines
#Start 26.03.2025, 20:00
#Finish 26.03.2025, 23:30

import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#F7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark1 = "✓"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text= "")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="Work")
        count_down(work_sec)
    if reps % 2 == 0:
        check_mark.config(text= check_mark1)
        timer_label.config(text="Short Break!", fg=PINK)
        count_down(short_break)
    if reps == 9:
        timer_label.config(text="Long Break!", fg=RED)
        count_down(long_break)
        reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    global reps
    global timer
    min_counter = math.floor(counter / 60)
    sec_counter = counter % 60
    if int(sec_counter) <= 9:
        sec_counter = f"0{sec_counter}"
    if int(min_counter) <= 9:
        min_counter = f"0{min_counter}"
    canvas.itemconfig(timer_text, text=f"{min_counter}:{sec_counter}")
    if counter > 0:
        timer = window.after(1000, count_down, counter - 1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_mark.config(text= mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(background=YELLOW,pady=50, padx=100)


canvas = Canvas(background=YELLOW,width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold") )
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW,  font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)

start_button = Button(text="start", fg=GREEN, bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="reset", fg=RED, bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)



window.mainloop()
