# daily_reminder.py

# Prompt user for a single task
task = input("Enter your task for today: ")

# Prompt for priority level
priority = input("Enter the priority level (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (unknown priority level)"

# Use if statement to modify the reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the reminder
print(reminder)

# Optional: loop to ask if user wants another reminder (demonstrates while loop)
repeat = input("Do you want to review your task again? (yes/no): ").lower()
while repeat == "yes":
    print(reminder)
    repeat = input("Do you want to review your task again? (yes/no): ").lower()
