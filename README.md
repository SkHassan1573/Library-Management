# 📚 Library Management System

A simple **Library Management System** built with **Python, CustomTkinter, and MongoDB**.
The application provides a graphical interface to manage books and perform basic library operations such as adding, updating, deleting, searching, and viewing books.

---

## 📌 Project Overview

This project is a desktop-based Library Management System designed to make book management simple and easy.

The application connects to a local **MongoDB database** and stores book information in a `books` collection. The graphical user interface is created using **CustomTkinter**.

---

## ✨ Features

* ➕ Add new books
* ✏️ Update existing book information
* 🗑️ Delete books
* 🔍 Search books by Book ID or Title
* 📋 Display all books in a table
* 📊 Display total number of books
* 🧹 Clear input form
* 📖 Store book details in MongoDB
* 🖱️ Select a book from the table to load its details into the form

The application supports book fields including **Book ID, Title, Author, Genre, Year, Copies, and Status**.

---

## 🛠️ Technologies Used

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| 🐍 Python         | Main programming language        |
| 🎨 CustomTkinter  | Graphical User Interface         |
| 🗄️ MongoDB       | Database                         |
| 🍃 PyMongo        | Python-MongoDB connection        |
| 🖼️ Tkinter / ttk | Table and message box components |

---

## 🗄️ Database

The project uses a local MongoDB database.

**Database:**

```text
LibraryDB
```

**Collection:**

```text
books
```

MongoDB is connected through:

```text
mongodb://localhost:27017/
```

The application checks whether MongoDB is running before performing database operations.

---

## 📚 Book Information

Each book can contain the following information:

```text
Book ID
Title
Author
Genre
Year
Copies
Status
```

Available status options are:

```text
Available
Borrowed
Reserved
```

---

## 🔄 CRUD Operations

### ➕ Create

Add a new book to the MongoDB database.

The system checks that **Book ID and Title** are entered and also prevents duplicate Book IDs.

### 📖 Read

Display all books stored in the MongoDB `books` collection in a table.

The application also displays the total number of books.

### ✏️ Update

Update the information of an existing book using its Book ID.

### 🗑️ Delete

Delete a book using its Book ID after confirmation from the user.

---

## 🔍 Search Function

The application provides a search box that can search books using:

* Book ID
* Book Title

The search is case-insensitive.

---

## 🖥️ User Interface

The application contains two main sections:

### Book Form

The left side contains the form for entering:

* Book ID
* Title
* Author
* Genre
* Year
* Copies
* Status

It also contains:

**ADD | UPDATE | DELETE | CLEAR** buttons.

### Book Table

The right side contains:

* Search box
* Search button
* Show All button
* Total book counter
* Book data table
* Scroll bar

---

## 📁 Project Structure

```text
Library-Management/
│
├── LibraryManagement.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

Make sure you have installed:

* Python
* MongoDB Community Server
* PyMongo
* CustomTkinter

Install the Python libraries using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 1. Start MongoDB

Make sure your MongoDB server is running locally.

### 2. Clone the Repository

```bash
git clone https://github.com/SkHassan1573/Library-Management.git
```

### 3. Open the Project

```bash
cd Library-Management
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python LibraryManagement.py
```

---

## 🎥 Project Demo

A screen recording demonstrating the working of the Library Management System is available below.

**▶️ [Watch Project Demo](https://drive.google.com/file/d/1XlZYDZMY04zaTEVepN47MxcCSNxVXq1t/view?usp=sharing)**


---

## 🧪 Main Operations Demonstrated

The project demonstrates:

1. Adding a new book
2. Viewing books
3. Searching for a book
4. Selecting a book
5. Updating book details
6. Deleting a book
7. Clearing the form
8. Storing and retrieving data from MongoDB

---

## 📊 Application Flow

```text
User
  ↓
CustomTkinter GUI
  ↓
Python Application
  ↓
PyMongo
  ↓
MongoDB
  ↓
LibraryDB
  ↓
books Collection
```

---

## ⚠️ Error Handling

The application checks whether MongoDB is connected. If MongoDB is not running, it displays an error/warning to the user.

It also validates:

* Empty Book ID
* Empty Title
* Duplicate Book ID
* Book not found during update
* Book not found during deletion

---

## 🎯 Project Purpose

The main purpose of this project is to demonstrate how a **Python GUI application can interact with a MongoDB database** and perform CRUD operations through a simple user interface.

---

## 👨‍💻 Author

**SkHassan1573**

GitHub:
https://github.com/SkHassan1573

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
