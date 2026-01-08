"""
Integration tests for Habit Tracker.
Tests combining multiple components together.
"""

import pytest
import os
from src.habit import Habit
from src.storage import HabitDatabase
from src.analytics import analyze_performance


class TestIntegration:
    """Integration tests combining multiple components."""
    
    def test_create_and_save_habit(self):
        """Test creating a habit and saving to database."""
        # Create habit
        habit = Habit("Integration Test", "daily")
        habit.complete()
        
        # Save to database
        db = HabitDatabase("test_integration.db")
        db.save_habit(habit)
        
        # Load from database
        loaded_habits = db.load_all_habits()
        
        # Verify
        assert len(loaded_habits) == 1
        assert loaded_habits[0].name == "Integration Test"
        assert len(loaded_habits[0].completions) == 1
        
        # Cleanup
        db.delete_habit(habit.id)
        db.close()
        os.remove("test_integration.db")
    
    def test_analytics_with_database(self):
        """Test analytics functions with database data."""
        db = HabitDatabase("test_analytics.db")
        
        # Create test habits
        habit1 = Habit("Test Daily", "daily")
        habit2 = Habit("Test Weekly", "weekly")
        
        # Add completions
        from datetime import datetime, timedelta
        today = datetime.now()
        
        # Add 3 days to daily habit
        for i in range(3):
            habit1.completions.append(today - timedelta(days=i))
        
        # Add 2 weeks to weekly habit
        for i in range(2):
            habit2.completions.append(today - timedelta(weeks=i))
        
        # Save to database
        db.save_habit(habit1)
        db.save_habit(habit2)
        
        # Load and analyze
        habits =
