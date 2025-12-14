To-Do List Manager (File-Based)

A simple, menu-driven To-Do List Manager built using Python.
This project allows users to manage tasks from the command line with persistent storage using a text file.

Project Overview

This application helps users:

Add new tasks

View existing tasks

Mark tasks as completed

Remove tasks

Store tasks permanently using a .txt file

The program runs entirely in the terminal and follows clean, modular design principles.

Features

Menu-driven command line interface

Persistent task storage using a text file

Mark tasks as completed or pending

Input validation and error handling

Simple and readable task format

Clean separation of logic and user interaction

Task Storage Format

All tasks are stored in a file named tasks.txt.

Each task is stored on a separate line using the following format:

[ ] Task description   (Pending)
[✔] Task description  (Completed)


This format is easy to read and simple to update programmatically.

Technologies Used

Python

File handling (.txt)

Command Line Interface (CLI)

How to Run the Program

Make sure Python is installed on your system

Clone the repository or download the project files

Open a terminal in the project directory

Run the program using:

python todo.py


The tasks.txt file will be created automatically if it does not already exist.

Menu Options
1. Add a new task
2. View all tasks
3. Mark a task as done
4. Remove a task
5. Exit

Program Design

The menu controls program flow and user interaction

Each task operation is handled by a dedicated function

File data is always read, modified in memory, and rewritten safely

Input validation prevents crashes and incorrect operations

This structure follows real-world software design practices.

What You Learn From This Project

File handling and persistence in Python

Menu-driven program design

Input validation and error handling

Clean function-based architecture

Basic CRUD operations

Possible Future Improvements

Store tasks using JSON or a database

Add task priorities or deadlines

Implement search or filtering

Create a graphical or web interface

Author

Aryan Sonsurkar
First-year Computer Engineering student

Final Notes

This project is intentionally simple but designed using correct programming and software design principles. It is suitable for beginners while still demonstrating real-world logic and structure.