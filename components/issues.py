import tkinter as tk
from tkinter import ttk


class Issue(tk.Frame):
    def __init__(self, parent, book_id, book_name, member_id, member_name, update, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.book_id = book_id
        self.book_name = book_name
        self.member_id = member_id
        self.member_name = member_name
        self.update = update

        self.book_label = tk.Label(self, text=f"Book: {self.book_name}", font=('Arial', 14))
        self.book_id_label = tk.Label(self, text=f"Book ID: {self.book_id}", font=('Arial', 14))
        self.member_label = tk.Label(self, text=f"Member: {self.member_name}", font=('Arial', 14))
        self.member_id_label = tk.Label(self, text=f"Member ID: {self.member_id}", font=('Arial', 14))
        self.create_widgets()

    def create_widgets(self):
        # Issue ID

        # Book name
        self.book_label.grid(row=0, column=0, sticky="ew", padx=70, pady=5)

        # Book ID
        self.book_id_label.grid(row=0, column=1, sticky="ew", padx=70, pady=5)

        # Member name
        self.member_label.grid(row=0, column=2, sticky="ew", padx=70, pady=5)

        # Member ID
        self.member_id_label.grid(row=0, column=3, sticky="ew", padx=70, pady=5)

        # Return button
        return_button = ttk.Button(self, text="Return", command=self.return_book)
        return_button.grid(row=0, column=4, padx=10, pady=5)

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    def return_book(self):
        # Simulate returning a book
        new_quantity = 1  # Assuming returning increases the quantity by 1
        self.update(self.issue_id, self.book_id, self.book_name, self.member_id, self.member_name, new_quantity)

        # Optionally update UI or perform other actions upon return


