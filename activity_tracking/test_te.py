import datetime
import pytest
from activity_tracking.te import TimeEntry

# filepath: c:\Users\ppain\repos\python\freeCodeCampLearnPythonBeginners\pppTimesTracker\activity_tracking\test_te.py

def test_time_entry_constructor():
    start_time = datetime.datetime(2025, 1, 20, 13)
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "learning"
    notes = "Place notes here"
    duration = 0.0

    te = TimeEntry(start_time, stop_time, activity, notes, duration)

    assert te.start == start_time
    assert te.stop == stop_time
    assert te.activity == activity
    assert te.notes == notes
    assert te.duration == duration

def test_time_entry_constructor_with_string_start():
    start_time = "2025-01-20T13:00:00"
    stop_time = datetime.datetime(2025, 1, 20, 14, 5)
    activity = "learning"
    notes = "Place notes here"
    duration = 0.0

    te = TimeEntry(start_time, stop_time, activity, notes, duration)

    assert te.start == datetime.datetime.fromisoformat(start_time)
    assert te.stop == stop_time
    assert te.activity == activity
    assert te.notes == notes
    assert te.duration == duration

def test_time_entry_default_constructor():
    te = TimeEntry()

    assert isinstance(te.start, datetime.datetime)
    assert isinstance(te.stop, datetime.datetime)
    assert te.activity == ''
    assert te.notes == ''
    assert te.duration == 0.0

