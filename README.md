# Student Record Management System

A terminal-based **Student Record Management System** built with Python. This application allows educational institutions or administrators to manage student profiles, track marks across multiple subjects, compute subject-wise grades, and monitor class attendance metrics.

## 🚀 Features

The project is split into three core modules managed by a centralized main menu:

* **Student Management (`student.py`):** Handles student registrations, views existing records, updates profiles, and deletes student entries using unique registration numbers.
* **Marks Management (`marks_management.py`):** Tracks scores out of 100 for core subjects (*Python, Calculus, EVS, English*). It automatically calculates individual subject grades, total scores, overall percentages, and final pass/fail statuses.
* **Attendance Management (`attendance_management.py`):** Calculates and displays individual student attendance percentages based on overall conducted and attended classes.

---

## 📁 Repository Structure

Your project files should be structured as follows:
```text
├── main.py                    # Application entry point & main menu loop
├── student.py                 # Handles CRUD operations for student records
├── marks_management.py        # Manages student marks and generates mark sheets
└── attendance_management.py   # Computes and displays student attendance metrics
```

---

## 🛠️ Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites
* **Python 3.x** must be installed on your computer. You can check your version by running:
  ```bash
  python --version
  ```
* This project uses built-in Python standard libraries, so **no external packages or dependencies are required**.

### Execution
1. Clone or download all four Python files into the same directory.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   ```bash
   cd path/to/your/project-directory
   ```
4. Start the application by executing the main script:
   ```bash
   python main.py
   ```

---

## 💻 How To Use

When you launch `main.py`, you will interact with a text-based dashboard:

1. **Register a Student First:** Go to `1. Student Management` -> `1. Register Student` to input a registration number, name, branch, and semester. *(Note: Marks and attendance tracking require a registered number).*
2. **Input Marks:** Navigate to `2. Marks Management` -> `1. Enter/Update Marks` to store subject scores.
3. **Generate a Mark Sheet:** Select `2. View Grade Card` in the Marks section to output a fully formatted academic performance report.
4. **Check Attendance:** Choose `3. Attendance Management` from the main menu to calculate percentage metrics.

---

## 📝 License

This project is open-source and free to use.
