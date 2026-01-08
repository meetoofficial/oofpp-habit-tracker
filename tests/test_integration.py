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
        habits = db.load_all_habits()
        stats = analyze_performance(habits)
        
        # Verify analytics
        assert stats["total_habits"] == 2
        assert stats["daily_habits"] == 1
        assert stats["weekly_habits"] == 1
        assert stats["longest_streak"] == 3
        
        # Cleanup
        db.delete_habit(habit1.id)
        db.delete_habit(habit2.id)
        db.close()
        os.remove("test_analytics.db")
    
    def test_cli_commands_integration(self):
        """Test that CLI commands work together."""
        # This is a smoke test - just import and check no errors
        from src.cli import cli
        assert cli is not None
        assert hasattr(cli, 'commands')
    
    def test_complete_workflow(self):
        """Test complete workflow: create -> complete -> analyze."""
        # Create habits
        habits = [
            Habit("Workout", "daily"),
            Habit("Reading", "daily"),
            Habit("Planning", "weekly"),
        ]
        
        # Complete habits
        habits[0].complete()  # Today
        habits[0].complete()  # Should create another completion
        
        # Test analytics
        stats = analyze_performance(habits)
        assert stats["total_habits"] == 3
        assert stats["daily_habits"] == 2
        assert stats["weekly_habits"] == 1


if __name__ == "__main__":
    pytest.main([__file__])
