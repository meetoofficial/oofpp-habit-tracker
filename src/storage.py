"""Database storage for habits."""

class HabitDatabase:
    """Manages habit storage."""
    
    def __init__(self):
        self.habits = []
    
    def save_habit(self, habit):
        self.habits.append(habit)
        return self
    
    def load_all_habits(self):
        return self.habits
