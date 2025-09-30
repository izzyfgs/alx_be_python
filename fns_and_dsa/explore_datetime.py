```python
# explore_datetime.py
# Demonstrates the use of Python's datetime module for handling dates and times.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate and display a future date by adding days_to_add to current_date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
```
