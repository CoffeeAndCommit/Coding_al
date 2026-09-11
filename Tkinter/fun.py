import tkinter as tk
import random

window = tk.Tk()
window.title("Catch Me!")
window.geometry("500x400")

score = 0

def move_button():
    global score

    score += 1
    score_label.config(text=f"Score: {score}")

    x = random.randint(50, 400)
    y = random.randint(100, 330)

    button.place(x=x, y=y)

score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 20)
)
score_label.pack()

button = tk.Button(
    window,
    text="CLICK ME! 😈",
    font=("Arial", 15),
    command=move_button
)

button.place(x=200, y=200)

window.mainloop()