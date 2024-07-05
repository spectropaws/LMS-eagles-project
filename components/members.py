import tkinter as tk
from tkinter import ttk
from . import memberedit  # Assuming memberedit module for editing members


class Member(tk.Frame):
    def __init__(self, parent, member_id, member_name, update, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.id = member_id
        self.name = member_name
        self.update = update

        self.name_label = tk.Label(self, text=f"Name: {self.name}", font=('Arial', 14))
        self.create_widgets()

    def create_widgets(self):
        # ID of the member
        tk.Label(self, text=f"ID: {self.id}", font=('Arial', 14)).grid(row=0, column=0, sticky="ew", padx=70, pady=5)

        # Name of the member
        self.name_label.grid(row=0, column=1, sticky="ew", padx=70, pady=5)

        # Edit button
        edit_button = ttk.Button(self, text="Edit", command=self.edit_member)
        edit_button.grid(row=0, column=2, padx=10, pady=5)

        self.grid_columnconfigure((0, 1, 2), weight=1)

    def handle_submit_changes(self, new_name):
        # Update member information with new name
        self.name = new_name
        # Call function from services to update member in database
        self.update(self.id, self.name)

    def edit_member(self):
        edit_window = memberedit.EditWindow(self.parent, self.name, self.handle_submit_changes)
