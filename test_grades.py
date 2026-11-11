
import pytest
from grades import grade


# Test all boundary marks
@pytest.mark.parametrize("mark, expected", [
    (32, "F"),
    (33, "F"),
    (59, "D"),
    (60, "C"),
    (69, "C"),
    (70, "B"),
    (79, "B"),
    (80, "A"),
])


def test_grade(mark, expected):
    assert grade(mark) == expected


# Test invalid marks
@pytest.mark.parametrize("mark", [-1, 101, 150])


def test_invalid_marks(mark):
    with pytest.raises(ValueError):
        grade(mark)
