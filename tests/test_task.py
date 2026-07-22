from study_task_manager.task import Task


def test_task_to_dict() -> None:
    """A Task should be converted to a dictionary correctly."""
    task = Task(
        course="Programming",
        title="Final Project",
        deadline="2026-08-10",
    )

    assert task.to_dict() == {
        "course": "Programming",
        "title": "Final Project",
        "deadline": "2026-08-10",
        "completed": False,
    }