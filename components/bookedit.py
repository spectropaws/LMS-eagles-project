import tkinter as tk
from tkinter import ttk


class EditWindow(tk.Toplevel):
    def __init__(self, parent, current_name, current_quantity, submit_callback):
        super().__init__(parent)
        self.title("Edit Book")
 
        # Store current values
        self.current_name = tk.StringVar(value=current_name)
        self.current_quantity = tk.IntVar(value=current_quantity)

        # Label and Entry for changing name
        tk.Label(self, text="Change name:").pack(pady=5)
        self.name_entry = tk.Entry(self, textvariable=self.current_name)
        self.name_entry.pack(pady=5)

        # Label and Entry for changing quantity
        tk.Label(self, text="Change quantity:").pack(pady=5)
        self.quantity_entry = tk.Entry(self, textvariable=self.current_quantity)
        self.quantity_entry.pack(pady=5)

        # Submit button
        submit_button = ttk.Button(self, text="Submit", command=self.submit_changes)
        submit_button.pack(pady=10)

        self.submit_callback = submit_callback

    def submit_changes(self):
        # Retrieve updated values
        new_name = self.current_name.get()
        new_quantity = self.current_quantity.get()

        # Pass updated values back to main window or a callback function
        if self.submit_callback:
            self.submit_callback(new_name, new_quantity)

        # Close the edit window
        self.destroy()
