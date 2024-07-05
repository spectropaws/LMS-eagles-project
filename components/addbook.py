import tkinter as tk
from tkinter import ttk
import asyncio

class AddBook:
    def __init__(self, parent, add_callback):
        self.parent = parent
        self.add_callback = add_callback

        self.window = tk.Toplevel(parent)
        self.window.title("Add New Book")

        # Frame for padding
        padding_frame = ttk.Frame(self.window, padding="20 20 20 20")
        padding_frame.pack(expand=True, fill='both')

        

        # Book Name
        tk.Label(padding_frame, text="Book Name:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.book_name_entry = tk.Entry(padding_frame)
        self.book_name_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        # Quantity
        tk.Label(padding_frame, text="Quantity:").grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.quantity_entry = tk.Entry(padding_frame)
        self.quantity_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        # Add Button
        add_button = ttk.Button(padding_frame, text="Add", command=self.add_book)
        add_button.grid(row=3, columnspan=2, pady=20)

    async def add_book_async(self, book_name, quantity):
        try:
            # Assuming add_callback is an async function that adds the book
            await self.add_callback(book_name, quantity)
            print(f"Added book '{book_name}' with quantity '{quantity}'")
        except Exception as e:
            print(f"Failed to add book: {e}")

    def add_book(self):
        book_name = self.book_name_entry.get()
        quantity = int(self.quantity_entry.get())

        # Start an asyncio event loop if one isn't running
        asyncio.run(self.add_book_async(book_name, quantity))
        

        # Close the window after adding the book
        self.window.destroy()
