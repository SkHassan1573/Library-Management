import customtkinter as ctk
from tkinter import messagebox
from pymongo import MongoClient

try:
    client = MongoClient("localhost", 27017)
    db = client["LibraryDB"]
    books = db["books"]
    print("Connected to MongoDB!")
    connected = True
except:
    print("MongoDB not running!")
    connected = False

app = ctk.CTk()
app.title("My Library")
app.geometry("1000x600")

def clear_form():
    id_entry.delete(0, "end")
    title_entry.delete(0, "end")
    author_entry.delete(0, "end")
    genre_entry.delete(0, "end")
    year_entry.delete(0, "end")
    copies_entry.delete(0, "end")
    status_combo.set("Available")

def get_data():
    return {
        "book_id": id_entry.get(),
        "title": title_entry.get(),
        "author": author_entry.get(),
        "genre": genre_entry.get(),
        "year": year_entry.get(),
        "copies": copies_entry.get(),
        "status": status_combo.get()
    }

def show_books():
    for row in table.get_children():
        table.delete(row)
    
    if not connected:
        return
    
    count = 0
    for book in books.find({}, {"_id": 0}):
        table.insert("", "end", values=[
            book.get("book_id", ""),
            book.get("title", ""),
            book.get("author", ""),
            book.get("genre", ""),
            book.get("year", ""),
            book.get("copies", ""),
            book.get("status", "")
        ])
        count += 1
    
    total_label.configure(text=f"Total: {count} books")

def add_book():
    if not connected:
        messagebox.showerror("Error", "Database not connected!")
        return
    
    data = get_data()
    
    if data["book_id"] == "" or data["title"] == "":
        messagebox.showerror("Error", "Book ID and Title are required!")
        return
    
    if books.find_one({"book_id": data["book_id"]}):
        messagebox.showerror("Error", "Book ID already exists!")
        return
    
    books.insert_one(data)
    show_books()
    clear_form()
    messagebox.showinfo("Success", "Book added!")

def update_book():
    if not connected:
        messagebox.showerror("Error", "Database not connected!")
        return
    
    data = get_data()
    
    if data["book_id"] == "":
        messagebox.showerror("Error", "Enter Book ID!")
        return
    
    if not books.find_one({"book_id": data["book_id"]}):
        messagebox.showerror("Error", "Book not found!")
        return
    
    books.update_one({"book_id": data["book_id"]}, {"$set": data})
    show_books()
    messagebox.showinfo("Success", "Book updated!")

def delete_book():
    if not connected:
        messagebox.showerror("Error", "Database not connected!")
        return
    
    book_id = id_entry.get()
    
    if book_id == "":
        messagebox.showerror("Error", "Enter Book ID!")
        return
    
    book = books.find_one({"book_id": book_id})
    if not book:
        messagebox.showerror("Error", "Book not found!")
        return
    
    if messagebox.askyesno("Confirm", f"Delete '{book.get('title', book_id)}'?"):
        books.delete_one({"book_id": book_id})
        show_books()
        clear_form()
        messagebox.showinfo("Success", "Book deleted!")

def search_book():
    search_text = search_entry.get().strip()
    
    if search_text == "":
        show_books()
        return
    
    for row in table.get_children():
        table.delete(row)
    
    count = 0
    for book in books.find({
        "$or": [
            {"book_id": {"$regex": search_text, "$options": "i"}},
            {"title": {"$regex": search_text, "$options": "i"}}
        ]
    }, {"_id": 0}):
        table.insert("", "end", values=[
            book.get("book_id", ""),
            book.get("title", ""),
            book.get("author", ""),
            book.get("genre", ""),
            book.get("year", ""),
            book.get("copies", ""),
            book.get("status", "")
        ])
        count += 1
    
    total_label.configure(text=f"Found: {count}")

def select_book(event):
    selected = table.focus()
    if not selected:
        return
    
    values = table.item(selected)["values"]
    if not values:
        return
    
    clear_form()
    id_entry.insert(0, values[0])
    title_entry.insert(0, values[1])
    author_entry.insert(0, values[2])
    genre_entry.insert(0, values[3])
    year_entry.insert(0, values[4])
    copies_entry.insert(0, values[5])
    status_combo.set(values[6])

left_frame = ctk.CTkFrame(app, width=300)
left_frame.pack(side="left", fill="both", padx=10, pady=10)

ctk.CTkLabel(left_frame, text="BOOK FORM", font=("Arial", 18, "bold")).pack(pady=(10, 5))
ctk.CTkLabel(left_frame, text="Enter book details", font=("Arial", 11)).pack(pady=(0, 10))

ctk.CTkLabel(left_frame, text="Book ID *", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
id_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter ID", height=32)
id_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Title *", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
title_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Title", height=32)
title_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Author", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
author_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Author", height=32)
author_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Genre", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
genre_entry = ctk.CTkEntry(left_frame, placeholder_text="e.g., Fiction, Mystery", height=32)
genre_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Year", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
year_entry = ctk.CTkEntry(left_frame, placeholder_text="e.g., 2020", height=32)
year_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Copies", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
copies_entry = ctk.CTkEntry(left_frame, placeholder_text="Number of copies", height=32)
copies_entry.pack(fill="x", padx=20, pady=(0, 8))

ctk.CTkLabel(left_frame, text="Status", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
status_combo = ctk.CTkComboBox(left_frame, values=["Available", "Borrowed", "Reserved"], height=32)
status_combo.pack(fill="x", padx=20, pady=(0, 10))
status_combo.set("Available")

btn_frame = ctk.CTkFrame(left_frame)
btn_frame.pack(fill="x", padx=20, pady=5)

ctk.CTkButton(btn_frame, text="ADD", command=add_book, fg_color="green", height=32).pack(side="left", fill="x", expand=True, padx=(0, 3))
ctk.CTkButton(btn_frame, text="UPDATE", command=update_book, fg_color="blue", height=32).pack(side="left", fill="x", expand=True, padx=3)
ctk.CTkButton(btn_frame, text="DELETE", command=delete_book, fg_color="red", height=32).pack(side="left", fill="x", expand=True, padx=3)
ctk.CTkButton(btn_frame, text="CLEAR", command=clear_form, fg_color="orange", height=32).pack(side="left", fill="x", expand=True, padx=(3, 0))

right_frame = ctk.CTkFrame(app)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

search_frame = ctk.CTkFrame(right_frame)
search_frame.pack(fill="x", pady=(0, 10))

search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search by ID or Title...", height=32)
search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

ctk.CTkButton(search_frame, text="Search", command=search_book, width=80, height=32).pack(side="left", padx=(0, 5))
ctk.CTkButton(search_frame, text="Show All", command=show_books, width=80, height=32).pack(side="left")

total_label = ctk.CTkLabel(right_frame, text="Total Books: 0", font=("Arial", 12, "bold"))
total_label.pack(anchor="w", pady=(10, 5))

from tkinter import ttk

table_frame = ctk.CTkFrame(right_frame)
table_frame.pack(fill="both", expand=True)

columns = ("Book ID", "Title", "Author", "Genre", "Year", "Copies", "Status")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)

widths = [80, 150, 120, 100, 60, 60, 100]
for col, w in zip(columns, widths):
    table.heading(col, text=col)
    table.column(col, width=w)

scroll = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scroll.set)

table.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

table.bind("<<TreeviewSelect>>", select_book)

if connected:
    show_books()
else:
    messagebox.showwarning("Warning", "MongoDB not running!\nPlease start MongoDB.")

app.mainloop()