import tkinter as tk
from tkinter import ttk

class EditWindow(tk.Toplevel):
    def __init__(self, parent, current_name, submit_callback):
        super().__init__(parent)
        self.title("Edit Member")

        # Store current value
        self.current_name = tk.StringVar(value=current_name)

        # Frame for padding
        padding_frame = ttk.Frame(self, padding="20 20 20 20")
        padding_frame.pack(expand=True, fill='both')

        # Label and Entry for changing name
        ttk.Label(padding_frame, text="Change name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = ttk.Entry(padding_frame, textvariable=self.current_name)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Submit button
        submit_button = ttk.Button(padding_frame, text="Submit", command=self.submit_changes)
        submit_button.grid(row=1, columnspan=2, pady=10)

        self.submit_callback = submit_callback

    def submit_changes(self):
        # Retrieve updated value
        new_name = self.current_name.get()

        # Pass updated value back to main window or a callback function
        if self.submit_callback:
            self.submit_callback(new_name)

        # Close the edit window
        self.destroy()
