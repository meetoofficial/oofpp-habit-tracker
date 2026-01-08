"""
Unit tests for Habit class (OOP testing).
Covers habit creation, completion, and streak calculation.
"""

import pytest
from datetime import datetime, timedelta
from src.habit import Habit


class TestHabit:
    """Test cases for Habit class."""
    
    def test_habit_creation(self):
        """Test creating a new habit."""
        habit = Habit("Exercise", "daily")
        assert habit.name == "Exercise"
        assert habit.periodicity == "daily"
        assert habit.get_streak() == 0
        assert not habit.completions
    
    def test_habit_creation_invalid_periodicity(self):
        """Test creating habit with invalid periodicity."""
        with pytest.raises(ValueError):
            Habit("Invalid", "monthly")
    
    def test_complete_habit(self):
        """Test marking habit as completed."""
        habit = Habit("Read", "daily")
        habit.complete()
        assert len(habit.completions) == 1
        assert isinstance(habit.completions[0], datetime)
    
    def test_daily_streak_calculation(self):
        """Test streak calculation for daily habits."""
        habit = Habit("Meditation", "daily")
        
        # Add 5 consecutive days
        today = datetime.now()
        for i in range(5):
            completion_time = today - timedelta(days=i)
            habit.completions.append(completion_time)
        
        assert habit.get_streak() == 5
    
    def test_weekly_streak_calculation(self):
        """Test streak calculation for weekly habits."""
        habit = Habit("Weekly Review", "weekly")
        
        # Add 3 consecutive weeks
        today = datetime.now()
        for i in range(3):
            completion_time = today - timedelta(weeks=i)
            habit.completions.append(completion_time)
        
        assert habit.get_streak() == 3
    
    def test_broken_streak_daily(self):
        """Test broken streak detection for daily habits."""
        habit = Habit("Exercise", "daily")
        
        # Add completions with gap (broken streak)
        today = datetime.now()
        habit.completions.append(today)  # Today
        habit.completions.append(today - timedelta(days=3))  # 3 days ago
        # Missing yesterday and day before
        
        assert habit.get_streak() == 1  # Only today counts
    
    def test_broken_streak_weekly(self):
        """Test broken streak detection for weekly habits."""
        habit = Habit("Planning", "weekly")
        
        # Add completions with gap > 1 week
        today = datetime.now()
        habit.completions.append(today)  # This week
        habit.completions.append(today - timedelta(weeks=2))  # 2 weeks ago
        # Missing last week
        
        assert habit.get_streak() == 1  # Only this week counts
    
    def test_is_broken_method(self):
        """Test is_broken() method."""
        habit = Habit("Read", "daily")
        
        # No completions = broken
        assert habit.is_broken()
        
        # Recent completion = not broken
        habit.complete()
        assert not habit.is_broken()
        
        # Old completion = broken
        old_habit = Habit("Old", "daily")
        old_time = datetime.now() - timedelta(days=2)
        old_habit.complete(old_time)
        assert old_habit.is_broken()
    
    def test_string_representation(self):
        """Test __str__ method."""
        habit = Habit("Test", "daily")
        habit.complete()
        representation = str(habit)
        assert "Test" in representation
        assert "daily" in representation
        assert "Streak" in representation
    
    def test_repr_representation(self):
        """Test __repr__ method."""
        habit = Habit("Test", "weekly")
        representation = repr(habit)
        assert "Habit" in representation
        assert "Test" in representation
        assert "weekly" in representation


if __name__ == "__main__":
    pytest.main([__file__])
