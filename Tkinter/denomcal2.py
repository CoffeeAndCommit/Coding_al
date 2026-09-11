from tkinter import *
from tkinter import messagebox
# pyrefly: ignore [missing-import]
from PIL import Image, ImageTk
import os


# ==================================================
# MAIN WINDOW
# ==================================================

root = Tk()
root.title("Indian Denomination Counter")
root.geometry("650x450")
root.minsize(500, 400)
root.configure(bg="light blue")


# Make main window responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)


# ==================================================
# IMAGE
# ==================================================

image_path = os.path.join(
    os.path.dirname(__file__),
    "img.png"
)

upload = Image.open(image_path)

# Image size
upload = upload.resize((300, 300))

image = ImageTk.PhotoImage(upload)

image_label = Label(
    root,
    image=image,
    bg="light blue"
)

image_label.grid(
    row=0,
    column=0,
    padx=20,
    pady=10
)


# ==================================================
# WELCOME MESSAGE
# ==================================================

label1 = Label(
    root,
    text="Hey User! Welcome to Indian Denomination Counter Application.",
    bg="light blue",
    font=("Arial", 11)
)

label1.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


# ==================================================
# FUNCTION TO OPEN CALCULATOR
# ==================================================

def msg():

    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )

    if MsgBox == "ok":
        topwin()


# ==================================================
# START BUTTON
# ==================================================

button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="brown",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

button1.grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)


# ==================================================
# CALCULATOR WINDOW
# ==================================================

def topwin():

    top = Toplevel(root)

    top.title("Indian Denominations Calculator")
    top.geometry("600x500")
    top.minsize(400, 450)
    top.configure(bg="light grey")


    # ------------------------------------------------
    # Make calculator window responsive
    # ------------------------------------------------

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)

    for row in range(11):
        top.rowconfigure(row, weight=1)


    # ==================================================
    # TITLE
    # ==================================================

    title = Label(
        top,
        text="Indian Denomination Calculator",
        bg="light grey",
        font=("Arial", 16, "bold")
    )

    title.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=10
    )


    # ==================================================
    # ENTER AMOUNT
    # ==================================================

    amount_label = Label(
        top,
        text="Enter total amount (₹)",
        bg="light grey",
        font=("Arial", 11)
    )

    amount_label.grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="e"
    )


    amount_entry = Entry(
        top,
        font=("Arial", 11)
    )

    amount_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=5,
        sticky="w"
    )


    # ==================================================
    # DENOMINATIONS
    # ==================================================

    denominations = [
        500,
        200,
        100,
        50,
        20,
        10
    ]

    entries = []


    # ==================================================
    # CALCULATOR FUNCTION
    # ==================================================

    def calculator():

        try:

            amount = int(amount_entry.get())

            if amount < 0:

                messagebox.showerror(
                    "Error",
                    "Please enter a positive amount."
                )

                return


            # ------------------------------------------
            # Calculate notes
            # ------------------------------------------

            note500 = amount // 500
            amount %= 500

            note200 = amount // 200
            amount %= 200

            note100 = amount // 100
            amount %= 100

            note50 = amount // 50
            amount %= 50

            note20 = amount // 20
            amount %= 20

            note10 = amount // 10
            amount %= 10


            # ------------------------------------------
            # Put values in Entry boxes
            # ------------------------------------------

            notes = [
                note500,
                note200,
                note100,
                note50,
                note20,
                note10
            ]


            for entry, note in zip(entries, notes):

                entry.delete(0, END)
                entry.insert(END, note)


            # ------------------------------------------
            # Remaining amount
            # ------------------------------------------

            remaining_label.config(
                text=f"Remaining amount: ₹{amount}"
            )


        except ValueError:

            messagebox.showerror(
                "Error",
                "Please enter a valid number."
            )


    # ==================================================
    # CALCULATE BUTTON
    # ==================================================

    calculate_button = Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=5
    )

    calculate_button.grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )


    # ==================================================
    # HEADING
    # ==================================================

    heading = Label(
        top,
        text="Number of notes for each denomination",
        bg="light grey",
        font=("Arial", 12, "bold")
    )

    heading.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )


    # ==================================================
    # CREATE DENOMINATION ROWS
    # ==================================================

    for i, denomination in enumerate(denominations):


        # ----------------------------------------------
        # Denomination Label
        # ----------------------------------------------

        denomination_label = Label(
            top,
            text=f"₹{denomination}",
            bg="light grey",
            font=("Arial", 11)
        )

        denomination_label.grid(
            row=4 + i,
            column=0,
            padx=10,
            pady=5,
            sticky="e"
        )


        # ----------------------------------------------
        # Entry Box
        # ----------------------------------------------

        denomination_entry = Entry(
            top,
            font=("Arial", 11),
            width=15
        )

        denomination_entry.grid(
            row=4 + i,
            column=1,
            padx=10,
            pady=5,
            sticky="w"
        )


        # Save entry box
        entries.append(denomination_entry)


    # ==================================================
    # REMAINING AMOUNT
    # ==================================================

    remaining_label = Label(
        top,
        text="Remaining amount: ₹0",
        bg="light grey",
        font=("Arial", 11, "bold")
    )

    remaining_label.grid(
        row=10,
        column=0,
        columnspan=2,
        pady=10
    )


# ==================================================
# START PROGRAM
# ==================================================

root.mainloop()