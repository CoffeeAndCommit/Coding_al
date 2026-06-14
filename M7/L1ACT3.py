import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Example")

# Load the generated image using Pillow
image_path = "/Users/medhavi/.gemini/antigravity-ide/brain/5490f713-fbf7-476e-82f7-3ac183f57c11/tkinter_image_1781429247144.png"
pil_image = Image.open(image_path)
img = ImageTk.PhotoImage(pil_image)

label = tk.Label(window, image=img)
label.image = img  # keep a reference
label.pack()

window.mainloop()
