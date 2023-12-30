import tkinter as tk
from random import choice, randint

# window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()
# window.mainloop()

### WIDGETS
# Label - for displ. text or images
# label = tk.Label(text="Hello, Tkinter", foreground="white", background="black", height=10, width=20)
# label.pack()
# window.mainloop()

# color can be specified using hexadecimal RGB values and as a string ("orange", "blue", "yellow", etc.)
# foreground and background can be shortened to fg and bg respectively
# width and height are measured in text units (width and height of the char 0 (zero))

## Button
# button = tk.Button(text="Click me!", fg="yellow", bg="blue", height=10, width=20)
# button.pack()
# window.mainloop()

## Entry

# .get()
# .delete()
# .insert()

# for collecting one-line text entries
# window = tk.Tk()
# label = tk.Label(text="Name")
# entry = tk.Entry()
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# label.pack()
# entry.pack()
# name = entry.get()
# entry.delete(0) # deletes the first character of the entry text
# entry.delete(0, tk.End) deletes the whole entry
# entry.insert(0, "Python")
# window.mainloop()

# Text
# .get()
# .delete()
# .insert()

# text_window = tk.Tk()
# text_widget = tk.Text()
# text_widget.pack()
# text_widget.get("1.0", "1.5")
# # text_widget.delete(1.0) #delete the first char of the first line
# text_widget.insert(1.0, "O!")
# text_window.mainloop()

# .get() in text takes two arguments: 1. line number of a character (counted from 1), 2. position of char in that line
# (count starts at 0).
# text_widget.get("1.0", "1.5") gets the first 5 letters of the first line
# text_widget.get("1.0", tk.EDN) gets the whole text from the box

# Frame
# container for other widgets

# window = tk.Tk()
# frame = tk.Frame()
# label = tk.Label(master=frame)
# frame.pack()
#
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
# label_a = tk.Label(master=frame_a, text="I'm in frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_b, text="I'm in frame B")
# label_b.pack()
#
# frame_a.pack()
# frame_b.pack()
#
# window.mainloop()
# related widgets can be assigned to the same frame, so that if the frame is moved the widgets stay together


## Different border effects
# window = tk.Tk()
#
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.GROOVE
# }
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     # borderwidth param must be > 1
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
#
# window.mainloop()

## Review exercises
"""Write a program that displays a Button widget that is 50 x 25 text units. It should have a white background with blue
 text that reads 'Click me'"""
# window = tk.Tk()
# button = tk.Button(text="Click me!", height=25, width=50, bg="white", fg="blue")
# button.pack()
# window.mainloop()

"""Write a program that displays and Entry widget that is 40 text units wide and has white background and black text.
Use .insert() to display text in the Entry widget that reads "What is your name?"
"""
# window = tk.Tk()
# entry_name = tk.Entry(width=40, bg="white", fg="black")
# entry_name.insert(0, "What is your name?")
# entry_name.pack()
# window.mainloop()

## GEOMETRY MANAGERS
### .pack()
# window = tk.Tk()
# frame1 = tk.Frame(master=window, height=100, bg="red")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)
# frame with the parameter fill set to tk.X is responsive to resizing the window horizontally but not vertically
# fill can take on the following values: tk.X, tk.Y and tk.BOTH

# frame1 = tk.Frame(master=window, height=100, width=200, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, height=100, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, height=100, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# the side param can take on the following values: tk.LEFT, tk.RIGHT, tk.TOP, tk.BOTTOM
# it specifies on which side of the window the widget should be placed
# tk.TOP is the default value
# window.mainloop()

### .place()
# use to control the precise location of a widget in a window or a frame
# need to specify x and y, i.e. the x- and y-coordinates (in pixels) for the top left-hand corner of the widget

# layouts created with .place() are not responsive
# difficult to control the placement if many widgets in a window

# window = tk.Tk()
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
#
# label1 = tk.Label(text="I'm at (0,0)", bg="red", master=frame)
# label1.place(x=0, y=0)
#
# label2 = tk.Label(text="I'm at (75, 75)", bg="yellow", master=frame)
# label2.place(x=75, y=75)
#
# window.mainloop()

### .grid()
# splits a window/ frame into rows and columns
# rows and columns both start at 0

# window = tk.Tk()
#
# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75) # if all rows have the same weight they expands at the same rate
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j, padx=5, pady=5) # padx and pady are stated in pixels, adds padding outside the frames
#         label = tk.Label(master=frame, text=f"Row {i}\n Column {j}")
#         label.pack(padx=5, pady=5) # adds padding inside the frames

### Review Exercise (geometry managers)

# window = tk.Tk()
# window.title("Address Entry Form")
#
# form_frm = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# form_frm.pack()
#
# first_n_lbl = tk.Label(master=form_frm, text="First Name:")
# first_n_ent = tk.Entry(master=form_frm, width=50)
# first_n_lbl.grid(row=0, column=0, sticky="e")
# first_n_ent.grid(row=0, column=1)
#
# last_n_lbl = tk.Label(master=form_frm, text="Last Name: ")
# last_n_lbl.grid(row=1, column=0, sticky="e")
# last_n_ent = tk.Entry(master=form_frm, width=50)
# last_n_ent.grid(row=1, column=1)
#
#
# add1_lbl = tk.Label(master=form_frm, text="Address Line 1: ")
# add1_ent = tk.Entry(master=form_frm, width=50)
# add1_lbl.grid(row=2, column=0, sticky="e")
# add1_ent.grid(row=2, column=1)
#
# add2_lbl = tk.Label(master=form_frm, text="Address Line 2: ")
# add2_ent = tk.Entry(master=form_frm, width=50)
# add2_lbl.grid(row=3, column=0, sticky=tk.E)
# add2_ent.grid(row=3, column=1)
#
# city_lbl = tk.Label(master=form_frm, text="City: ")
# city_ent = tk.Entry(master=form_frm, width=50)
# city_lbl.grid(row=4, column=0, sticky=tk.E)
# city_ent.grid(row=4, column=1)
#
# state_lbl = tk.Label(master=form_frm, text="State/ Province: ")
# state_ent = tk.Entry(master=form_frm, width=50)
# state_lbl.grid(row=5, column=0, sticky=tk.E)
# state_ent.grid(row=5, column=1)
#
# postal_c_lbl = tk.Label(master=form_frm, text="Postal Code: ")
# postal_c_ent = tk.Entry(master=form_frm, width=50)
# postal_c_lbl.grid(row=6, column=0, sticky=tk.E)
# postal_c_ent.grid(row=6, column=1)
#
# country_lbl = tk.Label(master=form_frm, text="Country: ")
# country_ent = tk.Entry(master=form_frm, width=50)
# country_lbl.grid(row=7, column=0, sticky=tk.E)
# country_ent.grid(row=7, column=1)
#
# buttons_frm = tk.Frame()
# buttons_frm.pack(fill=tk.X, ipadx=5, ipady=5)
#
# submit_btn = tk.Button(master=buttons_frm, text="Submit")
# submit_btn.pack(side=tk.RIGHT, padx=10, pady=10)
#
# clear_btn = tk.Button(master=buttons_frm, text="Clear")
# clear_btn.pack(side=tk.RIGHT, padx=10)
#
# window.mainloop()

### MAKING APPS INTERACTIVE

# event (button click, etc.) --> event object (instance of a class repr the event) --> event handler (function)
# event handler is bound to an event because it's called every time an the event occurs
# each widget has a .bind() method that helps them handle an even with a proper event handler
# .bind takes two args: .bind(<event_name>, event handler>)

# Button .command() attribute


# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
#
# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"


# window = tk.Tk()
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# # bind the decrease function to the decrease button when a button instance is created using the command keyword arg
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase)
# # same as above with decrease
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# window.mainloop()

### REVIEW EXERCISES

"""(1) Write a program that displays a single button with the default background color and black text and reads "Click me!
When the user clicks the button, the button background should change color randomly selected from the following list 
colors = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]"""

# def change_bg_color():
#     colors = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
#     color_btn["bg"] = choice(colors)
#
#
# window = tk.Tk()
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)
#
# color_btn = tk.Button(master=window, text="Click me!", command=change_bg_color)
# color_btn.grid(row=0, column=0, sticky="nsew")
#
# window.mainloop()

"""(2) Write a program that simulates rolling a six-sided dice. There should be one button with the text "Roll".
When the user clicks the button, a random integer from 1 to 6 should be displayed"""
#
#
# def roll_dice():
#     random_num = randint(1, 8)
#     lbl_result["text"] = f"{random_num}"
#     btn_roll["bg"] = choice(["yellow", "blue", "green", "red", "orange"])
#
#
# window = tk.Tk()
#
# window.rowconfigure([0, 1], minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)
#
# btn_roll = tk.Button(master=window, text="Roll", command=roll_dice, borderwidth=3)
# btn_roll.grid(row=1, column=0, sticky="nsew")
#
# lbl_result = tk.Label(master=window)
# lbl_result.grid(row=0, column=0, sticky="nsew")
#
# window.mainloop()



