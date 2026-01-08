"""
Command Line Interface for Habit Tracker using Click framework.
Provides user-friendly commands for habit management.
"""

import click
from datetime import datetime, timedelta
from .habit import Habit
from .storage import HabitDatabase
from .analytics import *


@click.group()
def cli():
    """Habit Tracker CLI - Manage your daily and weekly habits."""
    pass


@cli.command()
@click.option('--name', required=True, help='Name of the habit')
@click.option('--periodicity', type=click.Choice(['daily', 'weekly']), required=True, 
              help='Tracking period (daily/weekly)')
def create(name, periodicity):
    """Create a new habit."""
    try:
        habit = Habit(name, periodicity)
        db = HabitDatabase()
        db.save_habit(habit)
        db.close()
        click.echo(f"✅ Created: {habit}")
    except Exception as e:
        click.echo(f"❌ Error: {e}")


@cli.command()
@click.option('--name', required=True, help='Name of the habit to complete')
def complete(name):
    """Mark a habit as completed today."""
    try:
        db = HabitDatabase()
        habits = db.load_all_habits()
        
        found = False
        for habit in habits:
            if habit.name == name:
                habit.complete()
                db.save_habit(habit)
                click.echo(f"✅ Completed: {name}")
                found = True
                break
        
        if not found:
            click.echo(f"❌ Habit '{name}' not found")
        
        db.close()
    except Exception as e:
        click.echo(f"❌ Error: {e}")


@cli.command(name='list')
def list_habits():
    """List all habits with their current status."""
    try:
        db = HabitDatabase()
        habits = db.load_all_habits()
        db.close()
        
        if not habits:
            click.echo("📭 No habits found. Create one with 'create' command.")
            return
        
        click.echo("📋 Your Habits:")
        for i, habit in enumerate(habits, 1):
            click.echo(f"  {i}. {habit}")
    except Exception as e:
        click.echo(f"❌ Error: {e}")


@cli.command()
def analytics():
    """Show detailed habit analytics."""
    try:
        db = HabitDatabase()
        habits = db.load_all_habits()
        db.close()
        
        if not habits:
            click.echo("📊 No habits to analyze.")
            return
        
        # Use functional programming functions
        daily = get_daily_habits(habits)
        weekly = get_weekly_habits(habits)
        longest_all = get_longest_streak_all(habits)
        stats = analyze_performance(habits)
        
        click.echo("📊 Analytics Report:")
        click.echo(f"  Total habits: {stats['total_habits']}")
        click.echo(f"  Daily habits: {stats['daily_habits']}")
        click.echo(f"  Weekly habits: {stats['weekly_habits']}")
        click.echo(f"  Longest streak: {stats['longest_streak']}")
        click.echo(f"  Broken habits: {stats['broken_habits']}")
        click.echo(f"  Completion rate: {stats['completion_rate']}")
        click.echo(f"  Average streak: {stats['average_streak']:.1f}")
        
        click.echo("\n  Individual Habits:")
        for habit in habits:
            longest = get_longest_streak_for_habit(habits, habit.name)
            click.echo(f"    • {habit.name}: Current streak {habit.get_streak()}, Longest {longest}")
    except Exception as e:
        click.echo(f"❌ Error: {e}")


@cli.command()
def generate_test_data():
    """Generate 5 predefined habits with 4 weeks of test data."""
    try:
        habits = [
            Habit("Morning Exercise", "daily"),
            Habit("Read 30 Minutes", "daily"),
            Habit("Weekly Planning", "weekly"),
            Habit("Meditation", "daily"),
            Habit("Family Dinner", "weekly"),
        ]
        
        db = HabitDatabase()
        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=4)
        
        click.echo("🎭 Generating test data (4 weeks)...")
        
        for habit in habits:
            current_date = start_date
            
            while current_date <= end_date:
                if habit.periodicity == "daily":
                    # Simulate 80% completion for daily habits
                    if hash(habit.name + current_date.strftime("%Y%m%d")) % 10 < 8:
                        habit.complete(current_date)
                    current_date += timedelta(days=1)
                else:  # weekly
                    # Simulate 90% completion for weekly habits
                    if hash(habit.name + current_date.strftime("%Y%W")) % 10 < 9:
                        habit.complete(current_date)
                    current_date += timedelta(weeks=1)
            
            db.save_habit(habit)
            click.echo(f"  • {habit.name}: {len(habit.completions)} completions")
        
        db.close()
        click.echo("✅ Generated 5 habits with 4 weeks of test data")
        click.echo("   Run 'list' and 'analytics' to see the results!")
    except Exception as e:
        click.echo(f"❌ Error: {e}")


if __name__ == "__main__":
    cli()
