import tkinter as tk
from tkinter import ttk
import asyncio


class AddMember:
    def __init__(self, parent, add_callback):
        self.parent = parent
        self.add_callback = add_callback

        self.window = tk.Toplevel(parent)
        self.window.title("Add New Member")

        # Frame for padding
        padding_frame = ttk.Frame(self.window, padding="20 20 20 20")
        padding_frame.pack(expand=True, fill='both')

        # Member Name
        tk.Label(padding_frame, text="Member Name:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.member_name_entry = tk.Entry(padding_frame)
        self.member_name_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        # Add Button
        add_button = ttk.Button(padding_frame, text="Add", command=self.add_member)
        add_button.grid(row=2, columnspan=2, pady=20)

    async def add_member_async(self, member_name):
        try:
            # Assuming add_callback is an async function that adds the member
            await self.add_callback(member_name)
            print(f"Added member '{member_name}'")
        except Exception as e:
            print(f"Failed to add member: {e}")

    def add_member(self):
        member_name = self.member_name_entry.get()

        # Start an asyncio event loop if one isn't running
        asyncio.run(self.add_member_async(member_name))
        

        # Close the window after adding the member
        self.window.destroy()
