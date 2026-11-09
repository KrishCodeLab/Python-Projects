# Automatic File Organizer

A Python-based utility that organizes files into categorized directories based on their file extensions.

## Overview

Automatic File Organizer is a command-line automation project designed to simplify file and directory management.

The application identifies files within a user-specified directory and organizes them into appropriate categories, such as Images, Documents, Videos, and Audio.

The project is being developed incrementally, with a focus on Python's built-in `os` module, file handling, path management, and exception handling.

## Current Features

### Phase 1: Directory Handling — Completed

    -Retrieved the current working directory using os.getcwd().

    -Accepted a user-defined directory path.

    -Constructed paths using os.path.join().

    -Validated directory paths using os.path.exists() and os.path.isdir().

    -Retrieved directory contents using os.listdir().

    -Identified files using os.path.isfile().

    -Identified directories using os.path.isdir().

    -Stored filenames and directory names in separate lists.

### Phase 2: File Extension Identification — Completed

    -Extracted filenames and extensions using os.path.splitext().

    -Separated filenames from their extensions.

    -Implemented case-insensitive extension comparison using .lower().

    -Identified file types based on their extensions.

    -Classified files such as .txt, .py, .java, and .jpg.

    -Stored filenames for further processing.
### Phase 3: Category Folder Creation

   -Created category folders dynamically based on file extensions.
   -Used `os.path.join()` to construct complete directory paths.
   -Checked whether category folders already exist using `os.path.exists()` and `os.path.isdir()`.
   -Created missing directories using `os.mkdir()`.
   -Avoided duplicate folder creation by checking directory existence before creating it.
   -Added support for files with different extensions:
     -`.txt` → `txt`
     -`.py` → `python`
     -`.java` → `java`
     -`.jpg` → `jpg`
     -Files without extensions → `NoExtensionFiles`

   

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
| 2     | File Extension Identification  | Completed |
| 3     | Category Folder Creation       | Completed |
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
