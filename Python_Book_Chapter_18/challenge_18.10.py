import tkinter as tk

window = tk.Tk()
window.title("Make your own poem!")
window.rowconfigure([0, 1, 2, 3], minsize=400)

# Frames
# greeting frame
frm_greeting = tk.Frame(master=window)
# form fields frame
frm_entries = tk.Frame(master=window)
# generate button frame
frm_generate = tk.Frame(master=window)
# results frame
frm_result = tk.Frame(master=window, borderwidth=5, relief=tk.GROOVE, padx=10, pady=5)

# Greeting label
lbl_greeting = tk.Label(master=frm_greeting, text="Enter your favorite words, separated by commas.", width=70)
# Form fields
lbl_nouns = tk.Label(master=frm_entries, text="Nouns:")
ent_nouns = tk.Entry(master=frm_entries, width=70)
lbl_verbs = tk.Label(master=frm_entries, text="Verbs: ")
ent_verbs = tk.Entry(master=frm_entries, width=70)
lbl_adj = tk.Label(master=frm_entries, text="Adjectives: ")
ent_adj = tk.Entry(master=frm_entries, width=70)
lbl_prep = tk.Label(master=frm_entries, text="Prepositions: ")
ent_prep = tk.Entry(master=frm_entries, width=70)
lbl_adv = tk.Label(master=frm_entries, text="Adverbs: ")
ent_adv = tk.Entry(master=frm_entries, width=70)
# Generate button
btn_generate = tk.Button(master=frm_generate, text="Generate")
# Results field
lbl_result = tk.Label(master=frm_result, text="Your poem: ", pady=10, padx=10)
# Save as button
btn_save = tk.Button(master=frm_result, text="Save to file")

# Layout
# frames
frm_greeting.pack(pady=5)
frm_entries.pack(pady=5, padx=10)
frm_generate.pack(pady=5)
frm_result.pack(fill=tk.X, padx=10)

# slave labels and entry fields
lbl_greeting.pack(pady=5)
lbl_nouns.grid(row=1, column=0, sticky="e", padx=8)
ent_nouns.grid(row=1, column=1)
lbl_verbs.grid(row=2, column=0, sticky="e", padx=8)
ent_verbs.grid(row=2, column=1)
lbl_adj.grid(row=3, column=0, sticky="e", padx=8)
ent_adj.grid(row=3, column=1, )
lbl_prep.grid(row=4, column=0, sticky="e", padx=8)
ent_prep.grid(row=4, column=1)
lbl_adv.grid(row=5, column=0, sticky="e", padx=8)
ent_adv.grid(row=5, column=1)
btn_generate.grid(row=6, column=1, sticky="ns", pady=5)

lbl_result.pack(pady=10)
btn_save.pack(side=tk.BOTTOM)

window.mainloop()
