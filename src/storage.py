"""
Database storage using SQLite for habit persistence.
Implements CRUD operations for habits and completions.
"""

import sqlite3
from datetime import datetime
from typing import List
from .habit import Habit


class HabitDatabase:
    """
    SQLite database manager for habit storage.
    
    Attributes:
        conn (sqlite3.Connection): Database connection
    """
    
    def __init__(self, db_path: str = "habits.db"):
        """
        Initialize database connection.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        """Create database tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                periodicity TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id TEXT NOT NULL,
                completed_at TIMESTAMP NOT NULL,
                FOREIGN KEY (habit_id) REFERENCES habits (id)
            )
        """)
        
        self.conn.commit()
    
    def save_habit(self, habit: Habit):
        """
        Save or update a habit in the database.
        
        Args:
            habit: Habit object to save
        """
        cursor = self.conn.cursor()
        
        # Save or update habit
        cursor.execute("""
            INSERT OR REPLACE INTO habits (id, name, periodicity, created_at)
            VALUES (?, ?, ?, ?)
        """, (habit.id, habit.name, habit.periodicity, habit.created_at))
        
        # Remove old completions and save new ones
        cursor.execute("DELETE FROM completions WHERE habit_id = ?", (habit.id,))
        
        for completion in habit.completions:
            cursor.execute(
                "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
                (habit.id, completion)
            )
        
        self.conn.commit()
    
    def load_all_habits(self) -> List[Habit]:
        """
        Load all habits from the database.
        
        Returns:
            List[Habit]: List of all habits with their completions
        """
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT id, name, periodicity, created_at FROM habits")
        habits_data = cursor.fetchall()
        
        habits = []
        for habit_id, name, periodicity, created_at in habits_data:
            # Create habit object
            habit = Habit(name, periodicity)
            habit.id = habit_id
            habit.created_at = datetime.fromisoformat(created_at) if created_at else datetime.now()
            
            # Load completions
            cursor.execute(
                "SELECT completed_at FROM completions WHERE habit_id = ? ORDER BY completed_at",
                (habit_id,)
            )
            completions = cursor.fetchall()
            habit.completions = [
                datetime.fromisoformat(comp[0]) if isinstance(comp[0], str) else comp[0]
                for comp in completions
            ]
            
            habits.append(habit)
        
        return habits
    
    def delete_habit(self, habit_id: str):
        """
        Delete a habit and its completions.
        
        Args:
            habit_id: ID of the habit to delete
        """
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
        cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        self.conn.commit()
    
    def close(self):
        """Close database connection."""
        self.conn.close()
