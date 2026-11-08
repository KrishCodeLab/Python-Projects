# Automatic File Organizer

A Python-based utility that organizes files into categorized directories based on their file extensions.

## Overview

Automatic File Organizer is a command-line automation project designed to simplify file and directory management.

The application identifies files within a user-specified directory and organizes them into appropriate categories, such as Images, Documents, Videos, and Audio.

The project is being developed incrementally, with a focus on Python's built-in `os` module, file handling, path management, and exception handling.

## Current Features

- Retrieve the current working directory using `os.getcwd()`.
- Accept a user-defined directory path.
- Validate directory paths using `os.path.exists()` and `os.path.isdir()`.
- Retrieve directory contents using `os.listdir()`.
- Identify files using `os.path.isfile()`.
- Identify directories using `os.path.isdir()`.
- Construct paths using `os.path.join()`.

## Planned Features

- Extract file extensions using `os.path.splitext()`.
- Define file categories and their supported    extensions.
- Create category directories automatically.
- Move files into their respective directories.
- Handle file operation exceptions.
- Generate an organization summary.
- Implement logging for file operations.

## Technology Stack
| Python 3            Core programming language     
| OS Module           File and directory      

## Project Structure

Python-Projects/
└── 01-Automatic-File-Organizer/
    ├── main.py
    ├── README.md
    └── .gitignore


## Getting Started

### Prerequisites

- Python 3.x
- Git
- Terminal or command-line interface

### Installation

Clone the main repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Python-Projects/01-Automatic-File-Organizer
```

Run the application:

```bash
python main.py
```

## Development Roadmap

| Phase | Description                    | Status    |
| ----- | ------------------------------ | --------- |
| 1     | Directory Handling             | Completed |
| 2     | File Extension Identification  | Upcoming  |
| 3     | Category Folder Creation       | Upcoming  |
| 4     | Automatic File Movement        | Upcoming  |
| 5     | Exception Handling             | Upcoming  |
| 6     | Complete Organizer Integration | Upcoming  |

## Learning Objectives

This project provides practical experience with:

- Python file system operations.
- Absolute and relative file paths.
- Directory traversal.
- File extension identification.
- File automation.
- Exception handling.
- Writing modular and maintainable Python code.

## Future Enhancements

- Custom file categories.
- Duplicate file detection.
- File organization reports.
- Logging and error tracking.
- Configuration-based file categorization.
- Improved command-line interface.

## Author

**Krushna Govardhane**

---

This project is part of my ongoing Python programming practice, focused on building practical automation tools and strengthening core programming concepts.
