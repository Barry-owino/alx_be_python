#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days):
    """
    Calculates and displays the date after a specified number of days from today.

    Parameters:
        days (int): The number of days to add to the current date.
    """
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Date after {days} days: {formatted_future_date}")

def main():
    """
    Main function to demonstrate datetime functionalities.
    """
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

