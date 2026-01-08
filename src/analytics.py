"""Analytics module using Functional Programming."""

def filter_by_periodicity(habits, period):
    """Filter habits by periodicity."""
    return [h for h in habits if h.periodicity == period]

def get_longest_streak_all(habits):
    """Get longest streak among all habits."""
    if not habits:
        return 0
    return max(h.get_streak() for h in habits)

def get_daily_habits(habits):
    """Get all daily habits."""
    return filter_by_periodicity(habits, "daily")

def get_weekly_habits(habits):
    """Get all weekly habits."""
    return filter_by_periodicity(habits, "weekly")
