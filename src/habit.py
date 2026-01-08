"""Habit class using Object-Oriented Programming."""

class Habit:
    """Represents a trackable habit."""
    
    def __init__(self, name, periodicity):
        """Initialize a new habit."""
        self.name = name
        self.periodicity = periodicity
        self.completions = []
    
    def complete(self):
        """Mark habit as completed."""
        self.completions.append("done")
        return self
    
    def get_streak(self):
        """Calculate current streak."""
        return len(self.completions)
    
    def __str__(self):
        return f"{self.name} ({self.periodicity}) - Streak: {self.get_streak()}"
