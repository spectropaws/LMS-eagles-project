from backend import services
import tkinter as tk
from tkinter import ttk

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

style = ttk.Style()
style.configure('TNotebook.Tab', font=('Arial', 14))
style.configure('TNotebook.Tab', padding=(10, 8))

notebook.add(dashboard_tab, text='Dashboard')
notebook.add(books_tab, text='Books')
notebook.add(members_tab, text='Members')

label1 = tk.Label(dashboard_tab, text='This is Tab 1')
label1.pack(padx=20, pady=20)

label2 = tk.Label(books_tab, text='This is Tab 2')
label2.pack(padx=20, pady=20)

notebook.pack(expand=True, fill='both')


app.mainloop()
