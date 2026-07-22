# Study Task Manager

[![Tests](https://github.com/267e109e-JIN/study-task-manager/actions/workflows/tests.yml/badge.svg)](https://github.com/267e109e-JIN/study-task-manager/actions/workflows/tests.yml)

A simple command-line tool for managing university assignments and deadlines.

## Features

- Add assignments with a course name, task title, and deadline
- Display assignments in deadline order
- Mark assignments as completed
- Delete assignments
- Save assignment data locally in JSON format
- Validate empty fields, date formats, and task numbers

## Installation

Clone the repository:

```bash
git clone https://github.com/267e109e-JIN/study-task-manager.git
cd study-task-manager
```

Install the application:

```bash
python -m pip install -e .
```

## Usage

Start the application:

```bash
study-task-manager
```

The following menu will be displayed:

```text
=== Study Task Manager ===
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

### Example

```text
Course name: Programming
Task title: Final Project
Deadline (YYYY-MM-DD): 2026-08-10

Task added successfully.
Programming - Final Project - 2026-08-10
```

Tasks are automatically displayed in deadline order.

## Development Setup

Install the project with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Running Tests

Run the unit tests with:

```bash
python -m pytest -v
```

Tests are also automatically executed by GitHub Actions whenever code is pushed to the `main` branch or a pull request is created.

## Data Storage

Task data is stored locally in a `tasks.json` file. This file is excluded from Git version control.

## License

This project is licensed under the MIT License.