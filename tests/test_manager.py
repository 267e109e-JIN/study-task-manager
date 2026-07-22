from pathlib import Path

import pytest

from study_task_manager.manager import (
    add_task,
    complete_task,
    delete_task,
    get_tasks_sorted,
    load_tasks,
)


def test_add_task_saves_task(tmp_path: Path) -> None:
    """Adding a task should save it to the JSON file."""
    data_file = tmp_path / "tasks.json"

    task = add_task(
        course=" Programming ",
        title=" Final Project ",
        deadline="2026-08-10",
        data_file=data_file,
    )

    assert task.course == "Programming"
    assert task.title == "Final Project"
    assert task.deadline == "2026-08-10"
    assert task.completed is False

    saved_tasks = load_tasks(data_file)

    assert len(saved_tasks) == 1
    assert saved_tasks[0] == task


def test_add_task_rejects_empty_course(tmp_path: Path) -> None:
    """An empty course name should cause an error."""
    data_file = tmp_path / "tasks.json"

    with pytest.raises(
        ValueError,
        match="Course name cannot be empty",
    ):
        add_task(
            course=" ",
            title="Final Project",
            deadline="2026-08-10",
            data_file=data_file,
        )


def test_add_task_rejects_empty_title(tmp_path: Path) -> None:
    """An empty task title should cause an error."""
    data_file = tmp_path / "tasks.json"

    with pytest.raises(
        ValueError,
        match="Task title cannot be empty",
    ):
        add_task(
            course="Programming",
            title=" ",
            deadline="2026-08-10",
            data_file=data_file,
        )


def test_add_task_rejects_invalid_deadline(tmp_path: Path) -> None:
    """A deadline in the wrong format should cause an error."""
    data_file = tmp_path / "tasks.json"

    with pytest.raises(
        ValueError,
        match="Deadline must be in YYYY-MM-DD format",
    ):
        add_task(
            course="Programming",
            title="Final Project",
            deadline="2026/08/10",
            data_file=data_file,
        )


def test_get_tasks_sorted_by_deadline(tmp_path: Path) -> None:
    """Tasks should be returned in deadline order."""
    data_file = tmp_path / "tasks.json"

    add_task(
        "Economics",
        "Report",
        "2026-08-20",
        data_file,
    )
    add_task(
        "Programming",
        "Final Project",
        "2026-08-10",
        data_file,
    )
    add_task(
        "Mathematics",
        "Exercise",
        "2026-08-15",
        data_file,
    )

    tasks = get_tasks_sorted(data_file)

    assert [task.deadline for task in tasks] == [
        "2026-08-10",
        "2026-08-15",
        "2026-08-20",
    ]


def test_complete_task(tmp_path: Path) -> None:
    """The selected task should be marked as completed."""
    data_file = tmp_path / "tasks.json"

    add_task(
        "Programming",
        "Final Project",
        "2026-08-10",
        data_file,
    )

    completed_task = complete_task(
        task_number=1,
        data_file=data_file,
    )

    assert completed_task.completed is True

    saved_tasks = load_tasks(data_file)

    assert saved_tasks[0].completed is True


def test_delete_task(tmp_path: Path) -> None:
    """The selected task should be removed."""
    data_file = tmp_path / "tasks.json"

    add_task(
        "Programming",
        "Final Project",
        "2026-08-10",
        data_file,
    )
    add_task(
        "Economics",
        "Report",
        "2026-08-20",
        data_file,
    )

    deleted_task = delete_task(
        task_number=1,
        data_file=data_file,
    )

    remaining_tasks = load_tasks(data_file)

    assert deleted_task.title == "Final Project"
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].title == "Report"


@pytest.mark.parametrize(
    "function",
    [complete_task, delete_task],
)
def test_invalid_task_number(
    tmp_path: Path,
    function,
) -> None:
    """An unavailable task number should cause an error."""
    data_file = tmp_path / "tasks.json"

    add_task(
        "Programming",
        "Final Project",
        "2026-08-10",
        data_file,
    )

    with pytest.raises(
        ValueError,
        match="Task number is out of range",
    ):
        function(
            task_number=2,
            data_file=data_file,
        )
        