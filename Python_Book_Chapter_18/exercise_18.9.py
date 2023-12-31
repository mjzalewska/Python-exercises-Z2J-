import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        contents = txt_edit.get("1.0", tk.END)
        output_file.write(contents)

    window.title(f"Simple Text Editor - File Saved {filepath}")


window = tk.Tk()
window.title("Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(master=frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(master=frm_buttons, text="Save as...", command=save_file)
txt_edit = tk.Text(master=window, width=800)

frm_buttons.grid(row=0, column=0, sticky="ns")
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# padx and pady adds padding around the grid elements
# sticky set to ew forces the buttons to expand horizontally and fill the frame
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
