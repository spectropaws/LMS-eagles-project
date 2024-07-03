import tkinter as tk
from tkinter import ttk

class ScrollView(tk.Frame):
    def __init__(self, parent, width=400, height=300):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_widget(self, widget):
        widget.pack(in_=self.scrollable_frame, fill="x", padx=5, pady=5)


