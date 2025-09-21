# daily_reminder.py

# Ask the user to input their task
task = input("Enter your task: ")

# Ask for the task’s priority (high/medium/low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."