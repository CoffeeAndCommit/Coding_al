from tkinter import *

# Create Window
root = Tk()
root.title("Login App")
root.geometry("400x400")

# Create Frame
frame = Frame(root, height=220, width=360, bg="#d0efff")
frame.place(x=20, y=0)

# Labels
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Password", bg="#3895D3", fg="white", width=12)

# Entry Widgets
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function to show/hide password
def toggle_password():
    if pass_entry.cget("show") == "*":
        pass_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        pass_entry.config(show="*")
        show_btn.config(text="Show")

# Function when button is clicked
def display():
    # Clear previous message
    textbox.delete("1.0", END)

    name = name_entry.get()

    greet = f"Hey {name}"
    message = "\nCongratulations on your new account!"

    textbox.insert(END, greet)
    textbox.insert(END, message)

# Create Buttons
create_btn = Button(
    root,
    text="Create Account",
    command=display,
    bg="red",
    fg="white"
)

show_btn = Button(
    frame,
    text="Show",
    command=toggle_password
)

# Textbox
textbox = Text(root, height=5, width=40, bg="#BEBEBE")

# Place Labels
lbl1.place(x=20, y=20)
lbl2.place(x=20, y=80)
lbl3.place(x=20, y=140)

# Place Entries
name_entry.place(x=150, y=20)
email_entry.place(x=150, y=80)
pass_entry.place(x=150, y=140)

# Place Show Button
show_btn.place(x=280, y=137)

# Place Create Button
create_btn.place(x=130, y=230)

# Place Textbox
textbox.place(x=40, y=280)

# Start the GUI
root.mainloop()