import tkinter as tk
from tkinter import ttk
from . import bookedit


class Book(tk.Frame):
    def __init__(self, parent, book_id, book_name, total_quantity, issued_quantity, update, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.id = book_id
        self.name = book_name
        self.quantity = total_quantity
        self.issued = issued_quantity
        self.update = update

        self.name_label = tk.Label(self, text=f"Name: {self.name}", font=('Arial', 14))
        self.quantity_label = tk.Label(self, text=f"Quantity: {self.quantity}", font=('Arial', 14))
        self.create_widgets()

    def create_widgets(self):
        # ID of the book
        tk.Label(self, text=f"ID: {self.id}", font=('Arial', 14)).grid(row=0, column=0, sticky="ew", padx=70, pady=5)

        # Name of the book
        self.name_label.grid(row=0, column=1, sticky="ew", padx=70, pady=5)

        # Total quantity of the book
        self.quantity_label.grid(row=0, column=2, sticky="ew", padx=70, pady=5)

        # Issued quantity of the book
        tk.Label(self, text=f"Issued: {self.issued}", font=('Arial', 14)).grid(row=0, column=3, sticky="ew", padx=70, pady=5)

        # Edit button
        edit_button = ttk.Button(self, text="Edit", command=self.edit_book)
        edit_button.grid(row=0, column=4, padx=10, pady=5)

        # Issue button
        issue_button = ttk.Button(self, text="Issue", command=self.issue_book)
        issue_button.grid(row=0, column=5, padx=10, pady=5)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def handle_submit_changes(self, new_name, new_quantity):
        # Update book information with new values
        self.name = new_name
        self.quantity = new_quantity
        # call function from services to update book in database
        self.update(self.id, self.name, self.quantity)

    def edit_book(self):
        edit_window = bookedit.EditWindow(self.parent, self.name, self.quantity, self.handle_submit_changes)

    def issue_book(self):
        print(f"Issue button clicked for book ID: {self.id}")
