"""Command Line Interface for Habit Tracker."""

import click
from .habit import Habit
from .storage import HabitDatabase
from .analytics import *

db = HabitDatabase()

@click.group()
def cli():
    """Habit Tracker CLI"""

@cli.command()
@click.option('--name', required=True, help='Habit name')
@click.option('--periodicity', type=click.Choice(['daily', 'weekly']), required=True)
def create(name, periodicity):
    """Create a new habit."""
    habit = Habit(name, periodicity)
    db.save_habit(habit)
    click.echo(f"✅ Created: {habit}")

@cli.command()
def list_all():
    """List all habits."""
    habits = db.load_all_habits()
    if not habits:
        click.echo("No habits found.")
        return
    for habit in habits:
        click.echo(f"• {habit}")

@cli.command()
def analytics():
    """Show analytics."""
    habits = db.load_all_habits()
    daily = get_daily_habits(habits)
    weekly = get_weekly_habits(habits)
    longest = get_longest_streak_all(habits)
    
    click.echo("📊 Analytics Report:")
    click.echo(f"  Total habits: {len(habits)}")
    click.echo(f"  Daily habits: {len(daily)}")
    click.echo(f"  Weekly habits: {len(weekly)}")
    click.echo(f"  Longest streak: {longest}")

if __name__ == "__main__":
    cli()
