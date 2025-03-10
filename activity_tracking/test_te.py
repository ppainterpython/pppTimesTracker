import datetime
import pytest
from te import TimeEntry

# filepath: c:\Users\ppain\repos\python\freeCodeCampLearnPythonBeginners\pppTimesTracker\activity_tracking\test_te.py

def test_time_entry_constructor():
    start_time = datetime.datetime(2025, 1, 20, 13)
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "learning"
    notes = "Place notes here"

    te = TimeEntry(start_time, stop_time, activity, notes)

    assert te.start == start_time
    assert te.stop == stop_time
    assert te.activity == activity
    assert te.notes == notes
    assert te.duration == te.stop - te.start

def test_time_entry_constructor_with_string_start():
    start_time = "2025-01-20T13:00:00"
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "learning"
    notes = "Testing ISO string input for start time"

    te = TimeEntry(start_time, stop_time, activity, notes)

    assert te.start == datetime.datetime.fromisoformat(start_time), (
        f"Start time is not correct ISO conversion: {start_time} vs {te.start}")
    assert te.stop == stop_time, "Stop time is not correct"
    assert te.stop >= te.start, "Stop time is before start time"
    assert te.activity == activity, "Activity string is not correct"
    assert te.notes == notes, "Notes string is not correct"

def test_time_entry_constructor_with_string_stop():
    start_time = datetime.datetime(2025, 1, 20, 13, 5)
    stop_time = "2025-01-20T14:00:00"
    activity = "learning"
    notes = "Testing ISO string input for stop time"

    te = TimeEntry(start_time, stop_time, activity, notes)

    assert te.start == start_time, "Start time is not correct"
    assert te.stop == datetime.datetime.fromisoformat(stop_time), (
        f"Stop time is not correct ISO conversion: {stop_time} vs {te.stop}")
    assert te.activity == activity, "Activity string is not correct"
    assert te.notes == notes, "Notes string is not correct"
    assert te.duration == te.stop - te.start, "Duration is not correct"

def test_time_entry_constructor_with_zero_length_string_start():
    start_time = ""
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "Testing zero length string for start time"
    notes = "Testing"

    te = TimeEntry(start_time, stop_time, activity, notes)

    assert isinstance(te.start, datetime.datetime), "Start time is not correct"
    assert isinstance(te.stop, datetime.datetime), "Stop time is not a datetime object"
    assert te.activity == activity, "Activity string is not correct"
    assert te.notes == notes, "Notes string is not correct"
    assert te.duration == te.stop - te.start, "Duration is not correct"

def test_time_entry_constructor_with_zero_length_string_stop():
    start_time = datetime.datetime(2025, 1, 20, 14, 5)
    stop_time = ""
    activity = "Testing zero length string for stop time"
    notes = "Testing"

    te = TimeEntry(start_time, stop_time, activity, notes)

    assert isinstance(te.start, datetime.datetime), "Start time is not a datetime object"
    assert isinstance(te.stop, datetime.datetime), "Stop time is not a datetime object"
    assert te.activity == activity, "Activity string is not correct"
    assert te.notes == notes, "Notes string is not correct"
    assert te.duration == te.stop - te.start, "Duration is not correct"

def test_time_entry_constructor_with_invalid_iso_string_start():
    # Test invalid ISO format for start time
    start_time = "invalid-date-format"
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "learning"
    notes = "Place notes here"
    duration = 0.0

    with pytest.raises(ValueError):
        TimeEntry(start_time, stop_time, activity, notes)

    # Test invalid ISO format for stop time
    start_time = datetime.datetime(2025, 1, 20, 14, 5)
    stop_time = "invalid-date-format"

    with pytest.raises(ValueError):
        TimeEntry(start_time, stop_time, activity, notes)

def test_time_entry_default_constructor():
    te = TimeEntry()

    assert isinstance(te.start, datetime.datetime), "Start time is not a datetime object"
    assert isinstance(te.stop, datetime.datetime), "Stop time is not a datetime object"
    assert te.activity == '', "Default activity is not empty"
    assert te.notes == '', "Default notes are not empty"
    assert te.duration == datetime.timedelta(0), "Default duration is not zero"

