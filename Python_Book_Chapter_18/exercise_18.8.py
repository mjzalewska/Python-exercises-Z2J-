import tkinter as tk


def convert():
    """Convert the value from Fahrenheit to Celsius and insert the result into
    the lbl_result."""
    fah_value = float(ent_temperature.get())
    cel_value = (fah_value - 32) * 5 / 9
    lbl_result["text"] = f"{round(cel_value, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()

window.title("Temperature Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_f_symbol = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_f_symbol.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=3, padx=10)

window.mainloop()
