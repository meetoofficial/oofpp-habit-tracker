# Habit Tracker – Python Portfolio Project

A habit tracking backend application developed as part of the Object-Oriented and Functional Programming with Python (DLBDSOOFPP01) course.

This project demonstrates a hybrid programming approach, combining Object-Oriented Programming (OOP) for core business logic with Functional Programming (FP) for analytics and data processing.

##  Project Objectives

- Design a maintainable habit tracking system using Object-Oriented Programming
- Implement analytical functionality using pure Functional Programming
- Persist habit data across sessions using SQLite
- Provide a Command Line Interface (CLI) for user interaction
- Ensure correctness and reliability through automated testing

##  Features

- ✅ OOP Design: Habit class with encapsulated state and behavior
- ✅ Functional Analytics: Pure functions using map and filter
- ✅ SQLite Database: Persistent data storage
- ✅ CLI Interface: User-friendly command line using Click
- ✅ Automated Tests: Unit and integration tests (85%+ coverage)
- ✅ Test Fixtures: 5 predefined habits with 4 weeks of example data

## Architecture Overview

The application follows a clear separation of concerns:

- OOP Layer – models habits and behavior
- Functional Layer – performs analytics without side effects
- Persistence Layer – SQLite database storage
- Interface Layer – CLI interaction

CLI → OOP (Habit) → SQLite  
             ↓  
        Functional Analytics

##  Object-Oriented Design

The Habit class represents a habit and encapsulates the habit name, periodicity (daily or weekly), creation timestamp, completion history, streak calculation, and broken-habit detection logic.

## Functional Programming Analytics

Analytics are implemented as pure functions in analytics.py. These functions allow users to list all habits, filter habits by periodicity, retrieve the longest streak across all habits, and retrieve the longest streak for a specific habit. All analytics functions are side-effect free and do not mutate input data.

## Data Persistence

Habit data is persisted using a SQLite database with two tables: habits and completions. SQLite was chosen to ensure data integrity, structured storage, and persistence across user sessions.

##  Command Line Interface (CLI)

Create a habit:
python run.py create --name "Exercise" --periodicity daily

Complete a habit:
python run.py complete --name "Exercise"

List habits:
python run.py list

View analytics:
python run.py analytics

Generate predefined test data:
python run.py generate-test-data

##  Installation

Requirements:
- Python 3.7 or later

Installation steps:
git clone https://github.com/meetoefficial/oofpp-habit-tracker.git
cd oofpp-habit-tracker
pip install -r requirements.txt

##  Run the Application

python run.py

##  Testing

Run all tests:
pytest

Run tests with coverage:
pytest --cov=src --cov-report=term-missing

##  Project Structure

.
├── src/
├── tests/
├── data/
├── run.py
├── requirements.txt
└── README.md

## Academic Context

This project was developed for IU International University of Applied Sciences as part of the Object-Oriented and Functional Programming with Python (DLBDSOOFPP01) course. All acceptance criteria defined in the assignment are fulfilled.

##  Author

Khouloud Chebboubi  
B.A. Applied Artificial Intelligence  
IU International University of Applied Sciences

##  Conclusion

This project demonstrates a clean, testable, and maintainable habit tracking backend by combining Object-Oriented Programming with Functional Programming principles while fulfilling all academic requirements.
