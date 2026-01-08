"""
Unit tests for analytics module (FP testing).
Covers all functional programming functions.
"""

import pytest
from datetime import datetime, timedelta
from src.habit import Habit
from src.analytics import *


class TestAnalytics:
    """Test cases for analytics functions."""
    
    def setup_method(self):
        """Set up test data before each test."""
        self.habits = [
            Habit("Morning Exercise", "daily"),
            Habit("Read 30 Minutes", "daily"),
            Habit("Weekly Planning", "weekly"),
            Habit("Meditation", "daily"),
            Habit("Family Dinner", "weekly"),
        ]
        
        # Add streaks to test habits
        today = datetime.now()
        
        # Habit 0: 5-day streak
        for i in range(5):
            self.habits[0].completions.append(today - timedelta(days=i))
        
        # Habit 1: 3-day streak  
        for i in range(3):
            self.habits[1].completions.append(today - timedelta(days=i))
        
        # Habit 2: 4-week streak
        for i in range(4):
            self.habits[2].completions.append(today - timedelta(weeks=i))
    
    def test_filter_by_periodicity(self):
        """Test filtering habits by periodicity."""
        daily_habits = filter_by_periodicity(self.habits, "daily")
        assert len(daily_habits) == 3
        assert all(h.periodicity == "daily" for h in daily_habits)
        
        weekly_habits = filter_by_periodicity(self.habits, "weekly")
        assert len(weekly_habits) == 2
        assert all(h.periodicity == "weekly" for h in weekly_habits)
    
    def test_get_longest_streak_all(self):
        """Test finding longest streak among all habits."""
        longest = get_longest_streak_all(self.habits)
        assert longest == 5  # Morning Exercise has 5-day streak
    
    def test_get_longest_streak_for_habit(self):
        """Test finding streak for specific habit."""
        streak = get_longest_streak_for_habit(self.habits, "Read 30 Minutes")
        assert streak == 3
        
        # Test non-existent habit
        streak = get_longest_streak_for_habit(self.habits, "Non-Existent")
        assert streak == 0
    
    def test_get_daily_weekly_habits(self):
        """Test get_daily_habits and get_weekly_habits functions."""
        daily = get_daily_habits(self.habits)
        weekly = get_weekly_habits(self.habits)
        
        assert len(daily) == 3
        assert len(weekly) == 2
        assert daily[0].name == "Morning Exercise"
        assert weekly[0].name == "Weekly Planning"
    
    def test_analyze_performance(self):
        """Test comprehensive performance analysis."""
        stats = analyze_performance(self.habits)
        
        assert stats["total_habits"] == 5
        assert stats["daily_habits"] == 3
        assert stats["weekly_habits"] == 2
        assert stats["longest_streak"] == 5
        assert "completion_rate" in stats
        assert "average_streak" in stats
    
    def test_get_all_habits(self):
        """Test get_all_habits returns copy."""
        habits_copy = get_all_habits(self.habits)
        assert len(habits_copy) == len(self.habits)
        assert habits_copy is not self.habits  # Should be a copy
    
    def test_get_habit_names(self):
        """Test extracting habit names."""
        names = get_habit_names(self.habits)
        assert len(names) == 5
        assert "Morning Exercise" in names
        assert "Weekly Planning" in names


if __name__ == "__main__":
    pytest.main([__file__])
