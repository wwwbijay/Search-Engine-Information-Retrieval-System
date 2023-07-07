from tkinter import *
import tkinter as tk

bg_color = "#f3f3f3"
text_color = "#395f92"
font_family = "Tahoma"

window = tk.Tk()
window.title("Search Engine")
window.geometry("850x580")
window.configure(bg=bg_color)
window.resizable(0,0)
from PIL import ImageTk, Image
img=(Image.open("logo.png"))
imgg=img.resize((200,100))
imggg=ImageTk.PhotoImage(imgg)


lbl=Label(window,image=imggg,bg=bg_color)
lbl.pack(side=TOP)
# Create and position the search label
label = tk.Label(window, text="Search Author or Title:",fg=text_color,font=(font_family, 20,"italic"),bg=bg_color)
label.pack(pady=10)

# Create and position the search entry
entry = tk.Text(window,height=5,width=30,font=(font_family, 18))
entry.pack()

# Create and position the search button
button = tk.Button(window, text="Search",font=(font_family, 20),bg=text_color,fg="white")
button.pack(pady=10)


# Start the main event loop
window.mainloop()
