# School Management System

Project Overview

The School Management System is a Python-based application designed to manage student records, marks, report cards, class rankings, and teacher comments.

The application uses object-oriented programming, file handling, JSON data storage, logging, and automated testing with pytest.

Technologies Used

Programming Language: Python 3.14.6
Environment Manager: Anaconda / Conda 26.7.3
Virtual Environment: school_env
Testing Framework: pytest 9.0.3
Data Storage: JSON
Logging: Python Logging Module

## Project Structure

```text
Assignment_01/
│
├── project_01/
│   ├── __init__.py
│   ├── student.py
│   ├── reports.py
│   └── comments.py
│
│   
│
├── main.py
└── test_student.py
```

 Features

1. Add new students with unique roll numbers.
2. Add marks for six subjects.
3. Calculate student averages.
4. Assign grades based on average marks.
5. Generate individual student report cards.
6. Display class rankings based on average marks.
7. Generate teacher comments based on student performance.
8. Save and load student records using JSON.
9. Maintain application logs.
10. Validate user inputs and handle errors.
11. Run automated tests using pytest.

Environment Setup

1. Create Conda Environment

Create a Conda environment named `school_env`:

```bash
conda create -n school_env python=3.14.6
```

2. Activate Environment

```bash
conda activate school_env
```

3. Install pytest

```bash
python -m pip install pytest
```

4. Verify Python and pytest

```bash
python --version
python -m pytest --version
```

How to Run the Project

1. Activate the Environment

```bash
conda activate school_env
```

2. Navigate to Project Directory

```bash
cd /d E:\Assignment_01
```

3. Run the Application

```bash
python main.py
```

 
**Project:** School Management System  
**Date:** 10 November 2026
