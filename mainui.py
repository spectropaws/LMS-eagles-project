from backend import services
import tkinter as tk
from tkinter import ttk
from components.scrollview import ScrollView
from components.searchframe import SearchFrame
from components.books import Book
app = tk.Tk()
app.title("Authentication")
app.geometry("1500x900")
app.minsize(width=1500, height=900)

# Main Label
tk.Label(app, text="Library Manager", font=('Arial', 24)).pack(pady=30)

notebook = ttk.Notebook(app)

dashboard_tab = ttk.Frame(notebook)
books_tab = ttk.Frame(notebook)
members_tab = ttk.Frame(notebook)
issues_tab = ttk.Frame(notebook)


style = ttk.Style()
style.configure('TNotebook.Tab', font=('Arial', 14))
style.configure('TNotebook.Tab', padding=(10, 8))

notebook.add(dashboard_tab, text='Dashboard')
notebook.add(books_tab, text='Books')
notebook.add(members_tab, text='Members')
notebook.add(issues_tab, text='Issues')

label1 = tk.Label(dashboard_tab, text='This is Tab 1')
label1.pack(padx=20, pady=20)


notebook.pack(expand=True, fill='both')


# Books Tab
search_frame = SearchFrame(books_tab)
search_frame.pack(expand=True, fill=tk.X, padx=400, pady=0)
scroll_view = ScrollView(books_tab)
scroll_view.pack(expand=True, fill='both', padx=50, pady=(0, 50))


def update_book(book_id):
    # Find the Book instance by book_id and update its information
    for widget in scroll_view.scrollable_frame.winfo_children():
        if isinstance(widget, Book) and widget.id == book_id:
            widget.name_label.config(text=f"Name: {widget.name}")
            widget.quantity_label.config(text=f"Quantity: {widget.quantity}")


for i in range(10):
    book = Book(scroll_view.scrollable_frame, 213, "Grow penis", 50, 40, update_book)
    scroll_view.add_widget(book)
for i in range(10):
    book = Book(scroll_view.scrollable_frame, 213, "Grow penis with Johnny sins", 50, 40, update_book)
    scroll_view.add_widget(book)
for i in range(10):
    book = Book(scroll_view.scrollable_frame, 213, "Grow", 50, 40, update_book)
    scroll_view.add_widget(book)

scroll_view.pack(expand=True, fill='both', padx=50, pady=(0, 50))

# Update the scrollable_frame to fit its contents
scroll_view.scrollable_frame.update_idletasks()
app.mainloop()
