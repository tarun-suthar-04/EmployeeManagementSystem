import tkinter as tk
from tkinter import messagebox, ttk
from database.main import AddEmployee, UpdateEmployee, DeleteEmployee, FetchRecords

def run_menu():
    # your menu logic
    print("Menu launched")


# Add Employee Function
def add_employee():
    try:
        Id = int(entry_id.get())
        Name = entry_name.get()
        Salary = float(entry_salary.get())

        AddEmployee(Id, Name, Salary)
        messagebox.showinfo("Success", "Employee added successfully!")
        fetch_records()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Update Employee Function
def update_employee():
    try:
        Id = int(entry_id.get())
        Name = entry_name.get()
        Salary = float(entry_salary.get())

        UpdateEmployee(Id, Name, Salary)
        messagebox.showinfo("Success", "Employee updated successfully!")
        fetch_records()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Delete Employee Function
def delete_employee():
    try:
        Id = int(entry_id.get())
        DeleteEmployee(Id)
        messagebox.showinfo("Success", "Employee deleted successfully!")
        fetch_records()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Fetch and Display Records
def fetch_records():
    try:
        records = FetchRecords()
        tree.delete(*tree.get_children())  # clear old records
        for row in records:
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear input fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

# ---------------------- UI ----------------------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x400")

# Labels and Entry Fields
tk.Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Salary").grid(row=2, column=0, padx=10, pady=5)
entry_salary = tk.Entry(root)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Employee", command=add_employee).grid(row=3, column=0, pady=10)
tk.Button(root, text="Update Employee", command=update_employee).grid(row=3, column=1, pady=10)
tk.Button(root, text="Delete Employee", command=delete_employee).grid(row=3, column=2, pady=10)
tk.Button(root, text="Clear", command=clear_fields).grid(row=3, column=3, pady=10)

# Treeview to display employees
columns = ("Id", "Name", "Salary")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Id", text="ID")
tree.heading("Name", text="Name")
tree.heading("Salary", text="Salary")
tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Load records initially
fetch_records()

root.mainloop()

