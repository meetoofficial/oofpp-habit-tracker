"""Tests for Habit class."""

from src.habit import Habit

def test_habit_creation():
    habit = Habit("Exercise", "daily")
    assert habit.name == "Exercise"
    assert habit.periodicity == "daily"

def test_habit_completion():
    habit = Habit("Read", "daily")
    habit.complete()
    assert habit.get_streak() == 1
