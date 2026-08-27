# fundamental-booster
# 🧑‍💻 Interactive Personal Data Collector

## 📌 Project Overview
The **Interactive Personal Data Collector** is a Python-based console application that captures, processes, and displays personal information from the user. The system prompts the user for details such as **name, age, height, and favourite number**, then performs calculations and formatting to present a friendly summary.

This project is built to demonstrate core **Python fundamentals** including **`print()` and `input()` functions**, **data types**, **variables**, **operators**, **type casting**, and built-in functions like **`id()` and `type()`**.

---

## 🎯 Objectives
- Collect personal information interactively from the user
- Demonstrate fundamental Python concepts in a practical program
- Perform calculations and type conversions on user input
- Display clear, well-formatted, and user-friendly output

---

## 🛠️ Features
- 👋 Welcome message and program instructions
- ⌨️ Collects name, age, height, and favourite number from the user
- 🔢 Performs calculations using collected data (e.g., estimating birth year)
- 🔍 Displays the data type and memory address of each variable using `type()` and `id()`
- 📋 Prints a formatted summary of all collected information
- 🙏 Friendly exit/thank-you message
---
video link 
https://drive.google.com/file/d/1alLLBHh2hRgK19fSKlWb5WoI7w7w88LJ/view?usp=drive_link
---

## 📂 Data Collected
Each session gathers the following details from the user:
- **Name** (String)
- **Age** (Integer)
- **Height** (Float, in meters)
- **Favourite Number** (Integer)

---

## 🧠 Concepts Used

### ✅ Python Fundamentals
- Variables & Datatypes
- `print()` and `input()` functions
- Type Casting (`int()`, `float()`, `str()`)
- Operators (`+`, `-`, `*`, `/`)

### ✅ Data Types, Variables & Operators
- Storing each piece of collected information in an appropriately typed variable
- Using arithmetic operators to perform calculations (e.g., estimating birth year from age)
- Using string concatenation and formatted strings to build user-friendly output

### ✅ Type Casting
- Prompting the user for data and casting it to the correct type (e.g., casting age to an integer and height to a float)
- Converting data between types where needed and explaining the conversion clearly in the output (e.g., rounding a float to an integer for display)

### ✅ Built-in Functions
- `type()` to display the data type of each variable
- `id()` to display the memory address of each variable

---

## 🧾 Program Structure

```
Interactive_Personal_Data_Collector/
│
├── data_collector.py   # Main Python program
└── README.md            # Project documentation
```

---

## ▶️ How to Run the Program
1. Install **Python 3.x** on your system
2. Save the program file as `data_collector.py`
3. Open terminal / command prompt
4. Navigate to the project folder
5. Run the command:

```
python data_collector.py
```

---

## 🖥️ Sample Console Interaction
```
Welcome to the Interactive Personal Data Collector!

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140789847239568)
Age: 25 (Type: <class 'int'>, Memory Address: 9793456)
Height: 1.68 (Type: <class 'float'>, Memory Address: 140789847253232)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793312)

Your birth year is approximately: 1998 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!
```

---

## 🔐 Program Flow
1. **Welcome and Instructions** – Display a welcome message and a brief description of what the program does
2. **Collect Information** – Prompt the user to enter their name (string), age (integer), height (float), and favourite number (integer)
3. **Data Processing** – Perform calculations with user-provided data, such as determining the birth year based on age; print each variable's value, data type, and memory address using `type()` and `id()`
4. **Display Results** – Print a summary of the user's information, formatted in a user-friendly way; display messages showing how data types were converted where applicable
5. **Exit Message** – End with a thank-you message and encourage the user to explore Python further

---

## 🚀 Future Enhancements
- File handling using **CSV / JSON** to store collected data
- Input validation for stricter type and range checking
- GUI version using **Tkinter** or **PyQt**
- Support for collecting and comparing data from multiple users

---

## 👨‍💻 Author
Python Developer | apeksha

---

## 📄 License
This project is created for **educational purposes** and is free to use and modify.

---

✨ *Happy Coding!* ✨
