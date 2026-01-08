"""
Analytics module using Functional Programming paradigm.
Contains pure functions for habit analysis with no side effects.
"""

from typing import List, Dict, Any
from .habit import Habit


def get_all_habits(habits: List[Habit]) -> List[Habit]:
    """
    Return all habits (pure function example).
    
    Args:
        habits: List of habits
        
    Returns:
        List[Habit]: Copy of input list (no side effects)
    """
    return habits.copy()


def filter_by_periodicity(habits: List[Habit], period: str) -> List[Habit]:
    """
    Filter habits by periodicity using functional style.
    
    Args:
        habits: List of habits to filter
        period: 'daily' or 'weekly'
        
    Returns:
        List[Habit]: Filtered habits
        
    Example:
        >>> daily = filter_by_periodicity(habits, "daily")
    """
    return list(filter(lambda h: h.periodicity == period, habits))


def get_longest_streak_all(habits: List[Habit]) -> int:
    """
    Get the longest streak among all habits.
    
    Args:
        habits: List of habits
        
    Returns:
        int: Maximum streak length
        
    Example:
        >>> longest = get_longest_streak_all(habits)
    """
    streaks = list(map(lambda h: h.get_streak(), habits))
    return max(streaks) if streaks else 0


def get_longest_streak_for_habit(habits: List[Habit], habit_name: str) -> int:
    """
    Get the longest streak for a specific habit.
    
    Args:
        habits: List of habits
        habit_name: Name of the habit
        
    Returns:
        int: Streak length for the specified habit
        
    Example:
        >>> streak = get_longest_streak_for_habit(habits, "Exercise")
    """
    target_habits = list(filter(lambda h: h.name == habit_name, habits))
    return target_habits[0].get_streak() if target_habits else 0


def get_daily_habits(habits: List[Habit]) -> List[Habit]:
    """
    Get all daily habits.
    
    Args:
        habits: List of habits
        
    Returns:
        List[Habit]: Daily habits only
    """
    return filter_by_periodicity(habits, "daily")


def get_weekly_habits(habits: List[Habit]) -> List[Habit]:
    """
    Get all weekly habits.
    
    Args:
        habits: List of habits
        
    Returns:
        List[Habit]: Weekly habits only
    """
    return filter_by_periodicity(habits, "weekly")


def analyze_performance(habits: List[Habit]) -> Dict[str, Any]:
    """
    Generate comprehensive performance analytics.
    
    Args:
        habits: List of habits
        
    Returns:
        Dict: Performance metrics
        
    Example:
        >>> stats = analyze_performance(habits)
        >>> print(stats["longest_streak"])
    """
    if not habits:
        return {"error": "No habits available"}
    
    # Calculate metrics using functional programming
    daily = get_daily_habits(habits)
    weekly = get_weekly_habits(habits)
    streaks = list(map(lambda h: h.get_streak(), habits))
    broken = list(filter(lambda h: h.is_broken(), habits))
    
    return {
        "total_habits": len(habits),
        "daily_habits": len(daily),
        "weekly_habits": len(weekly),
        "longest_streak": max(streaks) if streaks else 0,
        "broken_habits": len(broken),
        "completion_rate": f"{(len(habits) - len(broken)) / len(habits) * 100:.1f}%" if habits else "0%",
        "average_streak": sum(streaks) / len(streaks) if streaks else 0,
    }


def get_habit_names(habits: List[Habit]) -> List[str]:
    """
    Extract habit names using map function.
    
    Args:
        habits: List of habits
        
    Returns:
        List[str]: Habit names
    """
    return list(map(lambda h: h.name, habits))
