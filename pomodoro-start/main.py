from tkinter import *
import math
import platform

if platform.system() == "Windows":
    import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
paused = False
paused_count = 0  # store remaining seconds when paused

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, paused, paused_count
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0
    paused = False
    paused_count = 0
    pause_button.config(text="Pause", state="disabled")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, paused, paused_count
    if paused:
        # If resuming from pause, use the saved paused_count
        count_down(paused_count)
        paused = False
        pause_button.config(text="Pause")
    else:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break = SHORT_BREAK_MIN * 60
        long_break = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break)
            title_label.config(text="Long Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)
    pause_button.config(state="normal")

# ---------------------------- PAUSE/RESUME ------------------------------- #
def pause_resume():
    global paused, paused_count
    if paused:
        # Resume
        start_timer()
    else:
        # Pause
        if timer:
            window.after_cancel(timer)
        paused = True
        paused_count = current_count
        pause_button.config(text="Resume")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, current_count
    current_count = count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0 and not paused:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        # Play sound on Windows only
        if platform.system() == "Windows":
            winsound.Beep(1000, 500)  # frequency, duration(ms)
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        pause_button.config(text="Pause", state="disabled")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

pause_button = Button(text="Pause", highlightthickness=0, state="disabled", command=pause_resume)
pause_button.grid(column=1, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
