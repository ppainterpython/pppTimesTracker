#-----------------------------------------------------------------------------+
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
        Calculated difference between stop and start times in hours

    Data Validation at Construction
    ------------------------------
    The constructor will validate the input types for start and stop times
    and calculate the duration as a datetime.timedelta object.
    If the start or stop time are a string, it is be converted to a 
    datetime object assuming a valid ISO format datetime.
    Empty strings for start or stop are set to the current datetime.
    If no stop time is provided, it defaults to the start time plus 30 minutes.
    The duration is calculated as the difference between the stop and start 
    times in hours. A negative value indicates the stop time is before the start
    time. 
    """

    duration: float = 0.0

    def __init__(self, start=datetime.datetime.now(), 
                 stop=datetime.datetime.now(), activity='', notes=''):
        """Full parameters Constructor for class TimeEntry
        
        Parameters
        ----------
        Same as the Attributes for the TimeEntry class
        """
        self.start = self.validate_datetime(start)
        self.stop = self.validate_datetime(stop)
        self.activity = activity
        self.notes = notes
        self.duration = self.stop - self.start

    def __str__(self):
        return f"{self.activity}"

    # Some static helper methods for input validation
    @staticmethod
    def validate_datetime(dt):
        """Validate if the input is a datetime object."""
        if isinstance(dt, datetime.datetime):
            return dt
        elif isinstance(dt, str):
            if len(dt) == 0:
                return datetime.datetime.now()
            return datetime.datetime.fromisoformat(dt)
        raise ValueError(f"Invalid datetime value: {dt}")
    

        
