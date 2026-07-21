from dataclasses import asdict, dataclass


@dataclass
class Task:
    """Represent a university assignment."""

    course: str
    title: str
    deadline: str
    completed: bool = False

    def to_dict(self) -> dict:
        """Convert the task to a dictionary."""
        return asdict(self)