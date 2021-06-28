from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    #global timer_text
    reps = 0
    timer_label["text"] = "Timer"
    checkmarks_label["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")

    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        window.bell()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        window.bell()
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN)
        window.bell()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks_label["text"] += "✔"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



window.after(1000, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmarks_label = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
checkmarks_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)



window.mainloop()
