from hypothesis import given, strategies as st
import pytest

from student_grades import average_marks, parse_srn, short_name


def valid_marks(s):
    try:
        marks = [int(m.strip()) for m in s.split(",")]
        return bool(s.strip()) and all(0 <= m <= 100 for m in marks)
    except (ValueError, AttributeError):
        return False


@given(st.lists(st.integers(0, 100), min_size=1).map(
    lambda x: ",".join(map(str, x))
))
def test_average_marks_valid(s):
    marks = [int(m) for m in s.split(",")]
    assert average_marks(s) == round(sum(marks) / len(marks), 2)


@given(st.one_of(st.none(), st.text()))
def test_average_marks_invalid(s):
    if not valid_marks(s):
        with pytest.raises(ValueError):
            average_marks(s)


def valid_srn(s):
    return (
        isinstance(s, str) and len(s) == 13
        and s[:4].isalpha() and s[4:6] == "UG"
        and s[6:8].isdigit() and s[8:10].isalpha()
        and s[10:].isdigit()
    )


@given(
    st.integers(0, 99),
    st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=2, max_size=2),
    st.integers(0, 999)
)
def test_parse_srn_valid(year, dept, number):
    srn = f"PES1UG{year:02d}{dept}{number:03d}"
    assert parse_srn(srn) == ("PES1", year, dept)


@given(st.one_of(st.none(), st.text()))
def test_parse_srn_invalid(s):
    if not valid_srn(s):
        with pytest.raises(ValueError):
            parse_srn(s)


@given(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1)
)
def test_short_name_valid(first, last):
    assert short_name(first + " " + last) == (
        first[0].upper() + ". " + last.capitalize()
    )


@given(st.text())
def test_short_name_invalid(s):
    parts = s.split()
    if len(parts) != 2 or not all(part.isalpha() for part in parts):
        with pytest.raises(ValueError):
            short_name(s)
