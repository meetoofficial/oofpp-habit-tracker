"""
Habit class using Object-Oriented Programming.
Defines the core Habit entity with tracking capabilities.
"""

import uuid
from datetime import datetime, timedelta
from typing import List, Optional


class Habit:
    """
    A habit that can be tracked daily or weekly.
    
    Attributes:
        id (str): Unique identifier
        name (str): Habit name
        periodicity (str): 'daily' or 'weekly'
        created_at (datetime): Creation timestamp
        completions (List[datetime]): List of completion times
    """
    
    def __init__(self, name: str, periodicity: str):
        """
        Initialize a new habit.
        
        Args:
            name: Name of the habit (e.g., "Morning Run")
            periodicity: Tracking period ('daily' or 'weekly')
        
        Raises:
            ValueError: If periodicity is not 'daily' or 'weekly'
        """
        if periodicity not in ['daily', 'weekly']:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions: List[datetime] = []
    
    def complete(self, completion_time: Optional[datetime] = None) -> 'Habit':
        """
        Mark the habit as completed.
        
        Args:
            completion_time: Optional specific time (defaults to now)
        
        Returns:
            self: For method chaining
        """
        if completion_time is None:
            completion_time = datetime.now()
        self.completions.append(completion_time)
        return self
    
    def get_streak(self) -> int:
        """
        Calculate the current streak length.
        
        Returns:
            int: Current streak count (0 if no completions)
            
        Note:
            - Daily habits: consecutive days
            - Weekly habits: consecutive weeks
            - Respects periodicity in calculation
        """
        if not self.completions:
            return 0
        
        # Sort completions newest first
        sorted_completions = sorted(self.completions, reverse=True)
        streak = 1
        
        for i in range(1, len(sorted_completions)):
            current = sorted_completions[i-1]
            previous = sorted_completions[i]
            
            if self.periodicity == "daily":
                # Check if consecutive days (exactly 1 day difference)
                if (current.date() - previous.date()).days == 1:
                    streak += 1
                else:
                    break
            else:  # weekly
                # Check if consecutive weeks (6-8 days difference)
                days_diff = (current.date() - previous.date()).days
                if 6 <= days_diff <= 8:
                    streak += 1
                else:
                    break
        
        return streak
    
    def is_broken(self) -> bool:
        """
        Check if the habit is currently broken.
        
        Returns:
            bool: True if habit is broken, False otherwise
        """
        if not self.completions:
            return True
        
        latest = max(self.completions)
        now = datetime.now()
        
        if self.periodicity == "daily":
            return (now.date() - latest.date()).days > 1
        else:  # weekly
            return (now.date() - latest.date()).days > 7
    
    def __str__(self) -> str:
        """String representation of the habit."""
        status = "✅ Active" if not self.is_broken() else "❌ Broken"
        return f"{self.name} ({self.periodicity}) - Streak: {self.get_streak()} - {status}"
    
    def __repr__(self) -> str:
        """Official representation."""
        return f"Habit(name='{self.name}', periodicity='{self.periodicity}', streak={self.get_streak()})"
