
import pytest

from student_grades import letter_grade, final_marks, exam_eligibility


# Letter-grade decision branches
@pytest.mark.parametrize(
    "marks, expected",
    [
        (-1, None),
        (101, None),
        (100, "S"),
        (90, "S"),
        (89, "A"),
        (80, "A"),
        (79, "B"),
        (70, "B"),
        (69, "C"),
        (60, "C"),
        (59, "D"),
        (50, "D"),
        (49, "E"),
        (40, "E"),
        (39, "F"),
        (0, "F"),
    ],
)
def test_grade_branches(marks, expected):
    if marks < 0 or marks > 100:
        with pytest.raises(ValueError, match="invalid marks"):
            letter_grade(marks)
    else:
        assert letter_grade(marks) == expected


# Final-marks validation and project-bonus branches
@pytest.mark.parametrize(
    "internal, external, project, expected",
    [
        (41, 30, False, None),
        (20, 61, False, None),
        (20, 30, False, 50),
        (20, 30, True, 55),
        (40, 60, True, 100),
        (40, 60, False, 100),
    ],
)
def test_final_marks_branches(internal, external, project, expected):
    if internal > 40 or external > 60:
        with pytest.raises(ValueError, match="marks out of range"):
            final_marks(internal, external, project)
    else:
        assert final_marks(internal, external, project) == expected


# Exam-eligibility decision branches
@pytest.mark.parametrize(
    "attendance, fees_paid, medical, expected",
    [
        (90, False, False, "blocked"),
        (75, True, False, "eligible"),
        (80, True, True, "eligible"),
        (65, True, True, "eligible"),
        (65, True, False, "detained"),
        (64, True, True, "detained"),
        (64, True, False, "detained"),
    ],
)
def test_exam_eligibility_branches(attendance, fees_paid, medical, expected):
    assert exam_eligibility(attendance, fees_paid, medical) == expected
