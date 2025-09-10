# 🏢 Employee Management System (Python + MySQL + Tkinter)

## 📌 Overview
The **Employee Management System** is a Python-based desktop application that allows users to manage employee records efficiently.  
It uses **MySQL** as the backend database and **Tkinter** for the user-friendly graphical interface.

## ✨ Features
- ➕ Add new employees (ID, Name, Salary)
- ✏️ Update employee details
- ❌ Delete employee records
- 📋 View all employees in a table (Treeview)
- ⚡ Real-time database connectivity with MySQL
- 🔒 Structured project with modular folders (config, database, ui, etc.)

## 🛠️ Tech Stack
- **Python 3.x**
- **MySQL** (Relational Database)
- **mysql-connector-python** (Database Driver) 
- **Tkinter** (GUI Library)

## 📂 Project Structure

EmployeeManagementSystem/
│── config/
│ └── db_config.py 
│
│── database/
│ └── db_connection.py 
│── ui/
│ └── menu.py 
│ └── test_connection.py 
│
│── venv/
│
│── README.md 

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tarun-suthar-04/EmployeeManagementSystem.git
   cd EmployeeManagementSystem

2. Create and activate the virtual Environment
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows

3. Install Dependencies
   ```
   pip install mysql-connector-python



## ⚙️ Database Setup
- **Login to MySQL and create the database + table:**

CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE Employee (
    Id INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL
);

## ⚙️ Configuration

**In config/db_config.py, update your database credentials:**

DB_CONFIG = {
    "host": "localhost",
    "user": "root", 
    "password": "yourpassword",  # eg:- 1234
    "database": "employee_db"
}

## 🚀 Run the Application
**Run the Tkinter-based menu interface:**
- python -m database.main




   
