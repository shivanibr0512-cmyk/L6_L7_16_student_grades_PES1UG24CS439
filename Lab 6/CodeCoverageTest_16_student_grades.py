
import pytest

from student_grades import letter_grade, final_marks, exam_eligibility


# Test all letter-grade categories and boundary values
@pytest.mark.parametrize(
    "marks, expected",
    [
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
def test_letter_grade_valid_marks(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_invalid_marks(marks):
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(marks)


# Test final marks with and without a project
def test_final_marks_without_project():
    assert final_marks(30, 40, False) == 70


def test_final_marks_with_project():
    assert final_marks(30, 40, True) == 75


def test_final_marks_project_cap():
    assert final_marks(40, 60, True) == 100


def test_final_marks_without_project_at_maximum():
    assert final_marks(40, 60, False) == 100


@pytest.mark.parametrize(
    "internal, external",
    [
        (41, 30),
        (20, 61),
    ],
)
def test_final_marks_out_of_range(internal, external):
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(internal, external, False)


# Test exam eligibility outcomes
def test_exam_blocked_when_fees_unpaid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_exam_eligible_with_attendance():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligible_with_medical_reason():
    assert exam_eligibility(65, True, True) == "eligible"


def test_exam_detained_without_medical_reason():
    assert exam_eligibility(64, True, False) == "detained"


def test_exam_detained_below_medical_attendance_threshold():
    assert exam_eligibility(64, True, True) == "detained"
