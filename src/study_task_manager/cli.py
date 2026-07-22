from .manager import (
    add_task,
    complete_task,
    delete_task,
    get_tasks_sorted,
)


def show_menu() -> None:
    """Display the main menu."""
    print()
    print("=== Study Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def add_task_interactively() -> None:
    """Ask the user for task information and add a task."""
    course = input("Course name: ")
    title = input("Task title: ")
    deadline = input("Deadline (YYYY-MM-DD): ")

    try:
        task = add_task(
            course=course,
            title=title,
            deadline=deadline,
        )

        print()
        print("Task added successfully.")
        print(
            f"{task.course} - "
            f"{task.title} - "
            f"{task.deadline}"
        )

    except ValueError as error:
        print(f"Error: {error}")


def show_tasks() -> bool:
    """Display all tasks sorted by deadline."""
    tasks = get_tasks_sorted()

    print()
    print("=== Tasks ===")

    if not tasks:
        print("No tasks found.")
        return False

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"

        print(
            f"{number}. "
            f"{task.course} - "
            f"{task.title} - "
            f"{task.deadline} - "
            f"{status}"
        )

    return True


def complete_task_interactively() -> None:
    """Ask the user which task should be completed."""
    if not show_tasks():
        return

    task_number_text = input("Task number to complete: ")

    try:
        task_number = int(task_number_text)
        task = complete_task(task_number)

        print()
        print("Task marked as completed.")
        print(f"{task.course} - {task.title}")

    except ValueError as error:
        print(f"Error: {error}")


def delete_task_interactively() -> None:
    """Ask the user which task should be deleted."""
    if not show_tasks():
        return

    task_number_text = input("Task number to delete: ")

    try:
        task_number = int(task_number_text)
        task = delete_task(task_number)

        print()
        print("Task deleted successfully.")
        print(f"{task.course} - {task.title}")

    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    """Run the application."""
    while True:
        show_menu()

        choice = input("Select: ").strip()

        if choice == "1":
            add_task_interactively()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            complete_task_interactively()

        elif choice == "4":
            delete_task_interactively()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print(
                "Invalid choice. "
                "Please select a number from 1 to 5."
            )


if __name__ == "__main__":
    main()