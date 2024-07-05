
import tkinter as tk
from tkinter import ttk
import asyncio


class AddIssue:
    def __init__(self, parent, add_callback, book_id=None, member_id=None):
        self.parent = parent
        self.add_callback = add_callback

        self.window = tk.Toplevel(parent)
        self.window.title("Add New Issue")

        # Frame for padding
        padding_frame = ttk.Frame(self.window, padding="20 20 20 20")
        padding_frame.pack(expand=True, fill='both')

        # Book ID
        tk.Label(padding_frame, text="Book ID:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.book_id_entry = tk.Entry(padding_frame)
        self.book_id_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        if book_id is not None:
            self.book_id_entry.insert(tk.END, book_id)

        # Member ID
        tk.Label(padding_frame, text="Member ID:").grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.member_id_entry = tk.Entry(padding_frame)
        self.member_id_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        if member_id is not None:
            self.member_id_entry.insert(tk.END, member_id)

        # Issue Button
        issue_button = ttk.Button(padding_frame, text="Issue", command=self.issue_book)
        issue_button.grid(row=3, columnspan=2, pady=20)

    async def add_issue_async(self, book_id, member_id):
        try:
            # Assuming add_callback is an async function that adds the issue
            await self.add_callback(book_id, member_id)
            print(f"Issued book with ID '{book_id}' to member with ID '{member_id}'")
        except Exception as e:
            print(f"Failed to issue book: {e}")

    def issue_book(self):
        book_id = self.book_id_entry.get()
        member_id = self.member_id_entry.get()

        # Start an asyncio event loop if one isn't running
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.create_task(self.add_issue_async(book_id, member_id))
        else:
            loop.run_until_complete(self.add_issue_async(book_id, member_id))

        # Close the window after issuing the book
        self.window.destroy()
