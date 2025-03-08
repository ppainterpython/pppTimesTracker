# te.py
import datetime

class TimeEntry:
    """
    A class to represent one entry of time spent doing some work.

    Attributes
    ----------
    start : datetime
        date and time an activity starts
    stop : datetime
        date and time an activity stops
    activity : str
        A unique activity identifier string, perhaps as a dictionary entry
        defining a list of activities that can be aggregated and summarized
    notes : str
        Additional descriptive text describing the particulars of this activity
    duration : float
        A fractional number of hours spent on this activity
    """

    def __init__(self):
        """Base Constructor for class TimeEntry"""
        self.start = datetime.datetime.now()
        self.stop = datetime.datetime.now()
        self.activity = ""
        self.notes = ""
        self.duration = 0.0

    def __init__(self, start: datetime, stop: datetime, activity: str, notes: str, duration: float):
        """Full parameters Constructor for class TimeEntry"""
        self.start = start
        assert isinstance(stop, object)
        self.stop = stop
        self.activity = activity
        self.notes = notes
        self.duration = duration


