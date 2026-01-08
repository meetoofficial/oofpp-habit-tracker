"""Tests for analytics functions."""

from src.habit import Habit
from src.analytics import *

def test_filter_by_periodicity():
    habits = [
        Habit("Exercise", "daily"),
        Habit("Planning", "weekly")
    ]
    daily = filter_by_periodicity(habits, "daily")
    assert len(daily) == 1
    assert daily[0].name == "Exercise"

def test_longest_streak():
    habits = [
        Habit("Habit1", "daily"),
        Habit("Habit2", "daily")
    ]
    habits[0].complete()
    habits[0].complete()
    longest = get_longest_streak_all(habits)
    assert longest == 2
