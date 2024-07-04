from tkinter import ttk
import tkinter as tk


class ScrollView(tk.Frame):
    def __init__(self, parent, width=400, height=300):
        super().__init__(parent)

        self.config(highlightthickness=2, highlightbackground="black")

        # Create a canvas and vertical scrollbar
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Create a frame within the canvas to hold scrollable content
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Place the scrollable_frame inside the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack canvas and configure resizing behavior
        self.canvas.pack(side="left", fill="both", expand=True)

        # Adjust scrollbar and canvas bindings
        self.bind("<Configure>", self.on_frame_configure)
        self.scrollable_frame.bind("<Configure>", lambda e: self.on_frame_configure())

    def on_frame_configure(self, event=None):
        # Update scroll region of canvas when the size of the scrollable frame changes
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_widget(self, widget):
        # Add a widget (e.g., Book) to the scrollable frame
        widget.pack(fill="x", padx=10, pady=5)

