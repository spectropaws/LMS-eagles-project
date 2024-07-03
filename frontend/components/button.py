import tkinter as tk
from tkinter import ttk

class StyledButton(tk.Frame):
    def __init__(self, parent, text, command, width=10, height=2, font=("Helvetica", 12), padding=5):
        super().__init__(parent)
        style = ttk.Style()
        style.configure("Custom.TButton", font=font, padding=padding)

        self.button = ttk.Button(self, text=text, command=command, style="Custom.TButton")
        self.button.config(width=width, padding=padding)
        self.button.pack(fill="x", padx=5, pady=5)