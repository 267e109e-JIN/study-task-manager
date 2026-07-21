from .manager import add_task, get_tasks_sorted


def show_menu() -> None:
    """Display the main menu."""
    print()
    print("=== Study Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")


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


def show_tasks() -> None:
    """Display all tasks sorted by deadline."""
    tasks = get_tasks_sorted()

    print()
    print("=== Tasks ===")

    if not tasks:
        print("No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"

        print(
            f"{number}. "
            f"{task.course} - "
            f"{task.title} - "
            f"{task.deadline} - "
            f"{status}"
        )


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
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()