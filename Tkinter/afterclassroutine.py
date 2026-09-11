import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("After-School Routine Checker")
window.geometry("400x300")


# List of routine tasks
routine = ["Homework", "Play", "Dinner", "Read a book"]


# Runs when a key is pressed
def key_pressed(event):
    if event.char:
        last_character.config(text="Last character: " + event.char)


# Runs when the routine area is clicked
def routine_clicked(event):
    click_message.config(text="You clicked the routine area! 👍")


# Runs when the button is clicked
def check_task():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task!"
        )
    else:
        next_task.config(text="Next task: " + routine[0])


# Heading
title = tk.Label(
    window,
    text="After-School Routine Checker",
    font=("Arial", 16)
)
title.pack(pady=10)


# Task entry box
task_entry = tk.Entry(window)
task_entry.pack(pady=5)

task_entry.bind("<Key>", key_pressed)


# Last character label
last_character = tk.Label(
    window,
    text="Last character: "
)
last_character.pack(pady=5)


# Routine area
routine_area = tk.Label(
    window,
    text="Click the Routine Area",
    bg="lightblue",
    width=30,
    height=3
)
routine_area.pack(pady=10)

routine_area.bind("<Button-1>", routine_clicked)


# Message after mouse click
click_message = tk.Label(
    window,
    text=""
)
click_message.pack()


# Button
button = tk.Button(
    window,
    text="Check My Routine",
    command=check_task
)
button.pack(pady=10)


# Next task
next_task = tk.Label(
    window,
    text="Next task: "
)
next_task.pack()


window.mainloop()