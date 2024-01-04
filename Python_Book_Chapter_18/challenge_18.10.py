import tkinter as tk
from random import choice
from tkinter.filedialog import asksaveasfilename


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Make your own poem!")
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
        self.btn_generate = tk.Button(master=self.frm_generate, text="Generate", command=self.run_app)
        self.btn_generate.grid(row=6, column=1, sticky="ns", pady=5)
        # Results field
        self.lbl_result = tk.Label(master=self.frm_result, text="Your poem: ", pady=10, padx=10)
        self.lbl_result.pack(pady=10)
        # Save as button
        self.btn_save = tk.Button(master=self.frm_result, text="Save to file", command=self.export_poem)
        self.btn_save.pack(side=tk.BOTTOM)

    def _validate_num_entries(self):
        """Checks if the number of entries in the entry field is correct. Returns True if it is and False otherwise"""
        entry_fields = {self.ent_nouns: 3, self.ent_verbs: 3, self.ent_adj: 3, self.ent_adv: 1, self.ent_prep: 3}
        return all(
            [False if len(field.get().split(",")) < min_elem else True for field, min_elem in entry_fields.items()])

    def _show_warning(self):
        """Shows a warning if the number of elements in any of the entry fields is below the minimum required number or
        the elements are not unique"""
        self.lbl_result["text"] = """
        Please check your input!
        I need at least 3 unique nouns, verbs, adjectives, prepositions and one unique adverb to generate a poem for you.
         """

    def _check_duplicates(self):
        """Checks duplicates among the words entered by the user. Returns True if duplicates found and False
        otherwise"""
        return all([(False if word_list.count(item) > 1 else True for item in word_list) for word_list in
                    self._get_word_lists()])

    def _get_word_lists(self):
        verb_list = self.ent_verbs.get().split(",")
        noun_list = self.ent_nouns.get().split(",")
        adj_list = self.ent_adj.get().split(",")
        prep_list = self.ent_prep.get().split(",")
        adv_list = self.ent_adv.get().split(",")

        return [verb_list, noun_list, adj_list, prep_list, adv_list]

    def _draw(self, elem_list, num_elem): #change due to max recursion error
        """Draws the required number of unique words"""
        chosen_elements = [choice(elem_list) for i in range(1, num_elem+1)]
        if len(set(chosen_elements)) >= 3:
            return chosen_elements
        else:
            self._draw(elem_list, 3-len(set(chosen_elements)))

    def _generate_poem(self):
        """Randomly selects at least 3 nouns, 3 verbs, 3 adjectives, 3 prepositions and one adverb from the elements
        provided by the user and generates a poem"""
        verbs, nouns, adj, prep, adv = self._get_word_lists()

        draw_verbs = self._draw(verbs, 3)
        draw_nouns = self._draw(nouns, 3)
        draw_adj = self._draw(adj, 3)
        draw_prep = self._draw(prep, 3)
        draw_adv = self._draw(adv, 1)

        vowels = ["a", "e", "i", "o", "u"]

        if adj[0][0] in vowels:
            self.lbl_result = (f"An {draw_adj[0]} {draw_nouns[0]}\n"
                               f"An {draw_adj[0]} {draw_nouns[0]} {draw_verbs[0]} {draw_prep[0]} the {draw_adj[1]} {draw_nouns[1]}\n"
                               f"{draw_adv[0]}, the {draw_nouns[0]} {draw_verbs[1]}"
                               f"the {draw_nouns[1]} {draw_verbs[2]} {draw_prep[1]} a {draw_adj[2]} {draw_nouns[2]}")
        else:
            self.lbl_result = (f"A {draw_adj[0]} {draw_nouns[0]}\n"
                               f"A {draw_adj[0]} {draw_nouns[0]} {draw_verbs[0]} {draw_prep[0]} the {draw_adj[1]} {draw_nouns[1]}\n"
                               f"{draw_adv[0]}, the {draw_nouns[0]} {draw_verbs[1]}"
                               f"the {draw_nouns[1]} {draw_verbs[2]} {draw_prep[1]} a {draw_adj[2]} {draw_nouns[2]}")

    def export_poem(self):
        """Saves the poem as a text file"""
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        else:
            with open(filepath, "w") as file:
                poem = self.lbl_result["text"]
                file.write(poem)

    def run_app(self):
        if not self._validate_num_entries() or not self._check_duplicates():
            self._show_warning()
        else:
            self._generate_poem()


if __name__ == '__main__':
    app = App()
    app.mainloop()
