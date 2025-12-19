# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")

# Loop to ensure valid priority
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid input. Please enter high, medium, or low.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)
