import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class SearchFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

    def create_widgets(self):
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self, textvariable=self.search_var, width=30, font=("Arial", 16))
        self.search_entry.grid(row=0, column=0, padx=5, pady=10, ipady=3, sticky="ew")

        search_image = Image.open("./images/search_icon.png")
        search_image = search_image.resize((30, 30), Image.BILINEAR)
        self.search_img = ImageTk.PhotoImage(search_image)
        self.search_button = ttk.Button(self, image=self.search_img, command=self.search)
        self.search_button.grid(row=0, column=1, padx=5)

        # Add Book button
        self.add_book_button = tk.Button(self, text="Add Book", command=self.add_book, font=("Arial", 16))
        self.add_book_button.grid(row=0, column=2, padx=5)

    def search(self):
        search_term = self.search_var.get()
        print(f"Searching for: {search_term}")

    def add_book(self):
        print("Add Book button clicked")
