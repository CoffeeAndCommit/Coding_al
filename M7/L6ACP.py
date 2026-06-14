import tkinter as tk
from tkinter import ttk, messagebox
import random

# ---------------------------
# Game logic
# ---------------------------
choices = ["Rock", "Paper", "Scissors"]


def decide_winner(user_choice: str, comp_choice: str) -> str:
    """Return result string based on classic R‑P‑S rules."""
    if user_choice == comp_choice:
        return "Tie!"
    if (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        return "You Win!"
    return "Computer Wins!"


def play(choice: str):
    comp = random.choice(choices)
    result = decide_winner(choice, comp)
    lbl_user_choice.config(text=f"You: {choice}")
    lbl_comp_choice.config(text=f"Computer: {comp}")
    lbl_result.config(text=result)

# ---------------------------
# UI Layout (premium look)
# ---------------------------
root = tk.Tk()
root.title("Rock‑Paper‑Scissors")
root.geometry("380x420")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# Title
ttk.Label(root, text="Rock‑Paper‑Scissors", font=("Helvetica", 18, "bold"), background="#f0f4f8").pack(pady=20)

# Frame for buttons
frame_btn = tk.Frame(root, bg="#f0f4f8")
frame_btn.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=8)

for opt in choices:
    ttk.Button(frame_btn, text=opt, command=lambda o=opt: play(o)).pack(side="left", padx=10)

# Display area
lbl_user_choice = ttk.Label(root, text="You: —", font=("Helvetica", 12), background="#f0f4f8")
lbl_user_choice.pack(pady=10)

lbl_comp_choice = ttk.Label(root, text="Computer: —", font=("Helvetica", 12), background="#f0f4f8")
lbl_comp_choice.pack(pady=10)

lbl_result = ttk.Label(root, text="Result —", font=("Helvetica", 14, "bold"), foreground="#0066CC", background="#f0f4f8")
lbl_result.pack(pady=20)

# Reset button
ttk.Button(root, text="Reset", command=lambda: (
    lbl_user_choice.config(text="You: —"),
    lbl_comp_choice.config(text="Computer: —"),
    lbl_result.config(text="Result —")
)).pack(pady=10)

root.mainloop()
