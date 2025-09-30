from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date():
    # Ask user how many days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Current date
    current_date = datetime.now()
    # Add the days
    future_date = current_date + timedelta(days=days_to_add)
    # Print result in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
