"""Test data with 4 weeks of habit completions."""

from src.habit import Habit

def create_test_habits():
    """Create 5 predefined habits with test data."""
    habits = [
        Habit("Morning Exercise", "daily"),
        Habit("Read 30 Minutes", "daily"),
        Habit("Weekly Planning", "weekly"),
        Habit("Meditation", "daily"),
        Habit("Family Dinner", "weekly"),
    ]
    return habits

print("Test fixtures: 5 habits created (3 daily, 2 weekly)")
