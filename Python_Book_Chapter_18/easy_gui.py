import easygui as gui

## msgbox()
# print(gui.msgbox(msg="Hello!", title="My first message box", ok_button="Click me"))

## buttonbox()
# print(gui.buttonbox(msg="Please choose the desired color", title="Color choice", choices=["Blue", "Red", "Yellow"]))

## indexbox()
colors = ["Blue", "Red", "Yellow"]
# when choices defined outside of function the indices can later be referenced elsewhere
# print(gui.indexbox(msg="Please choose the desired color", title="Color choice", choices=colors))

# enterbox()
# print(gui.enterbox(msg="Please probvide your email address: ", title="Email address"))

# fileopenbox()
# print(gui.fileopenbox(title="Please select a file"))
# returns the absolute path or None if the user closes the dialogue box w/o choosing anything

# diropenbox()
# print(gui.diropenbox(title="Please choose a directory"))
# returns None if the user exits w/o pressing open or save
# doesn't actually open anything - only returns the absolute path

# filesavebox()
# print(gui.filesavebox(title="Save file"))
# must choose a specific file

## Review exercises:
#(1)
# print(gui.buttonbox(title="Watch out!", choices=["I'll be careful"]))
#(2)
# print(gui.enterbox(msg="What is your name?"))

