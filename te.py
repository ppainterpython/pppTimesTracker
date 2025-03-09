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

    def __init__(self, start=datetime.datetime.now(), 
                 stop=datetime.datetime.now(), activity='', notes='', 
                 duration=0.0):
        """Full parameters Constructor for class TimeEntry
        
        Parameters
        ----------
        Same as the Attributes for the TimeEntry class
        """
        if isinstance(start, datetime.datetime):
            self.start = start
        elif isinstance(start, str):
            self.start = datetime.datetime.fromisoformat(start)
        self.stop = stop
        self.activity = activity
        self.notes = notes
        self.duration = duration

    def __str__(self):
        return f"{self.activity}"

