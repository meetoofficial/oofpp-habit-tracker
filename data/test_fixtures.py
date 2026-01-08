"""
Test data fixtures - 4 weeks of predefined habit data.
Used for unit testing streak calculations.
"""

from datetime import datetime, timedelta
from src.habit import Habit


def create_predefined_habits():
    """
    Create 5 predefined habits with 4 weeks of tracking data.
    
    Returns:
        List[Habit]: 5 habits (3 daily, 2 weekly) with 4 weeks of completions
    """
    habits = [
        Habit("Morning Exercise", "daily"),
        Habit("Read 30 Minutes", "daily"),
        Habit("Weekly Planning", "weekly"),
        Habit("Meditation", "daily"),
        Habit("Family Dinner", "weekly"),
    ]
    
    # Generate 4 weeks of data (from 4 weeks ago to today)
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=4)
    
    # Completion patterns (simulating real usage)
    patterns = {
        "Morning Exercise": 0.85,  # 85% completion
        "Read 30 Minutes": 0.75,   # 75% completion
        "Weekly Planning": 0.95,   # 95% completion
        "Meditation": 0.65,        # 65% completion
        "Family Dinner": 0.90,     # 90% completion
    }
    
    # Add completions based on patterns
    for habit in habits:
        completion_rate = patterns[habit.name]
        current_date = start_date
        
        while current_date <= end_date:
            if habit.periodicity == "daily":
                # Simulate daily completion based on rate
                if hash(f"{habit.name}{current_date.date()}") % 100 < completion_rate * 100:
                    habit.completions.append(current_date)
                current_date += timedelta(days=1)
            else:  # weekly
                # Simulate weekly completion based on rate
                if hash(f"{habit.name}{current_date.isocalendar().week}") % 100 < completion_rate * 100:
                    habit.completions.append(current_date)
                current_date += timedelta(weeks=1)
    
    return habits


def get_test_fixture_stats():
    """
    Get statistics about test fixtures.
    
    Returns:
        dict: Statistics about the test data
    """
    habits = create_predefined_habits()
    
    stats = {
        "total_habits": len(habits),
        "daily_count": sum(1 for h in habits if h.periodicity == "daily"),
        "weekly_count": sum(1 for h in habits if h.periodicity == "weekly"),
        "total_completions": sum(len(h.completions) for h in habits),
        "date_range": "4 weeks",
        "habits": [h.name for h in habits]
    }
    
    return stats


if __name__ == "__main__":
    # Demo: Show test fixture statistics
    print("🧪 Test Fixture Statistics")
    print("=" * 40)
    
    habits = create_predefined_habits()
    stats = get_test_fixture_stats()
    
    print(f"Total habits: {stats['total_habits']}")
    print(f"Daily habits: {stats['daily_count']}")
    print(f"Weekly habits: {stats['weekly_count']}")
    print(f"Total completions: {stats['total_completions']}")
    print(f"Date range: {stats['date_range']}")
    
    print("\n" + "=" * 40)
    print("Individual Habit Details:")
    
    for habit in habits:
        print(f"\n{habit.name} ({habit.periodicity}):")
        print(f"  Completions: {len(habit.completions)}")
        print(f"  Current streak: {habit.get_streak()}")
        print(f"  Status: {'Active' if not habit.is_broken() else 'Broken'}")
