# User Interface
import inventory
import db
import tkinter as tk 
from tkinter import messagebox


# --------------------
# APP START
# --------------------
db.create_db() 

root = tk.Tk()
root.title("Midterm Group Project - Inventory and Sales Management System")
root.geometry("1100x520")

left = tk.Frame(root)
left.pack(side="left", padx=15, pady=15)

right = tk.Frame(root)
right.pack(side="right", padx=15, pady=15, fill="both", expand=True)

root.mainloop()