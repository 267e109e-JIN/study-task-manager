import json
from datetime import datetime
from pathlib import Path

from .task import Task


DEFAULT_DATA_FILE = Path("tasks.json")


def load_tasks(data_file: Path = DEFAULT_DATA_FILE) -> list[Task]:
    """Load tasks from a JSON file."""
    if not data_file.exists():
        return []

    with data_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [Task(**item) for item in data]


def save_tasks(
    tasks: list[Task],
    data_file: Path = DEFAULT_DATA_FILE,
) -> None:
    """Save tasks to a JSON file."""
    with data_file.open("w", encoding="utf-8") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            ensure_ascii=False,
            indent=2,
        )


def add_task(
    course: str,
    title: str,
    deadline: str,
    data_file: Path = DEFAULT_DATA_FILE,
) -> Task:
    """Create a new task and save it."""
    if not course.strip():
        raise ValueError("Course name cannot be empty.")

    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(
            "Deadline must be in YYYY-MM-DD format."
        ) from exc

    task = Task(
        course=course.strip(),
        title=title.strip(),
        deadline=deadline,
    )

    tasks = load_tasks(data_file)
    tasks.append(task)
    save_tasks(tasks, data_file)

    return task


def get_tasks_sorted(
    data_file: Path = DEFAULT_DATA_FILE,
) -> list[Task]:
    """Return all tasks sorted by deadline."""
    tasks = load_tasks(data_file)

    return sorted(
        tasks,
        key=lambda task: datetime.strptime(
            task.deadline,
            "%Y-%m-%d",
        ),
    )
def complete_task(
    task_number: int,
    data_file: Path = DEFAULT_DATA_FILE,
) -> Task:
    """Mark a task as completed using its displayed number."""
    tasks = get_tasks_sorted(data_file)

    if not 1 <= task_number <= len(tasks):
        raise ValueError("Task number is out of range.")

    task = tasks[task_number - 1]
    task.completed = True

    save_tasks(tasks, data_file)

    return task


def delete_task(
    task_number: int,
    data_file: Path = DEFAULT_DATA_FILE,
) -> Task:
    """Delete a task using its displayed number."""
    tasks = get_tasks_sorted(data_file)

    if not 1 <= task_number <= len(tasks):
        raise ValueError("Task number is out of range.")

    deleted_task = tasks.pop(task_number - 1)
    save_tasks(tasks, data_file)

    return deleted_task