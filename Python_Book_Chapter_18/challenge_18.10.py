import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Make your own poem!"
        self.rowconfigure([0, 1, 2, 3], minsize=400)

        # Frames
        # greeting frame
        self.frm_greeting = tk.Frame(master=self)
        self.frm_greeting.pack(pady=5)
        # form fields frame
        self.frm_entries = tk.Frame(master=self)
        self.frm_entries.pack(pady=5, padx=10)
        # generate button frame
        self.frm_generate = tk.Frame(master=self)
        self.frm_generate.pack(pady=5)
        # results frame
        self.frm_result = tk.Frame(master=self, borderwidth=5, relief=tk.GROOVE, padx=10, pady=5)
        self.frm_result.pack(fill=tk.X, padx=10)

        # Greeting label
        self.lbl_greeting = tk.Label(master=self.frm_greeting, text="Enter your favorite words, separated by commas.",
                                     width=70)
        self.lbl_greeting.pack(pady=5)
        # Form fields
        # Nouns
        self.lbl_nouns = tk.Label(master=self.frm_entries, text="Nouns:")
        self.ent_nouns = tk.Entry(master=self.frm_entries, width=70)
        self.lbl_nouns.grid(row=1, column=0, sticky="e", padx=8)
        self.ent_nouns.grid(row=1, column=1)
        # Verbs
        self.lbl_verbs = tk.Label(master=self.frm_entries, text="Verbs: ")
        self.ent_verbs = tk.Entry(master=self.frm_entries, width=70)
        self.lbl_verbs.grid(row=2, column=0, sticky="e", padx=8)
        self.ent_verbs.grid(row=2, column=1)
        # Adjectives
        self.lbl_adj = tk.Label(master=self.frm_entries, text="Adjectives: ")
        self.ent_adj = tk.Entry(master=self.frm_entries, width=70)
        self.lbl_adj.grid(row=3, column=0, sticky="e", padx=8)
        self.ent_adj.grid(row=3, column=1, )
        # Prepositions
        self.lbl_prep = tk.Label(master=self.frm_entries, text="Prepositions: ")
        self.ent_prep = tk.Entry(master=self.frm_entries, width=70)
        self.lbl_prep.grid(row=4, column=0, sticky="e", padx=8)
        self.ent_prep.grid(row=4, column=1)
        # Adverbs
        self.lbl_adv = tk.Label(master=self.frm_entries, text="Adverbs: ")
        self.ent_adv = tk.Entry(master=self.frm_entries, width=70)
        self.lbl_adv.grid(row=5, column=0, sticky="e", padx=8)
        self.ent_adv.grid(row=5, column=1)
        # Generate button
        self.btn_generate = tk.Button(master=self.frm_generate, text="Generate")
        self.btn_generate.grid(row=6, column=1, sticky="ns", pady=5)
        # Results field
        self.lbl_result = tk.Label(master=self.frm_result, text="Your poem: ", pady=10, padx=10)
        self.lbl_result.pack(pady=10)
        # Save as button
        self.btn_save = tk.Button(master=self.frm_result, text="Save to file")
        self.btn_save.pack(side=tk.BOTTOM)

    def validate_entries(self, required_elem_num):
        """Checks if the number of entries in the entry field is correct. Returns True if it is and False if it isn't"""

        # for field, num_elem in entry_fields:
        #     if len(field.get()) < num_elem:
        #         field.delete(0, tk.END)
        #         field.insert(f"The minimum required number of elements in this field is {num_elem}")

    def show_warning(self):
        pass

    def check_duplicates(self):
        """Checks duplicates among the words entered by the user and displays a warning message if any found"""

    def generate_poem(self):
        """Randomly selects at least 3 nouns, 3 verbs, 3 adjectives, 3 prepositions and one adverb from the elements
        provided by the user and generates a poem"""

    def export_poem(self):
        """Saves the poem as a text file"""


# window = tk.Tk()
# window.title("Make your own poem!")
# window.rowconfigure([0, 1, 2, 3], minsize=400)


if __name__ == '__main__':
    app = App()
    app.mainloop()
