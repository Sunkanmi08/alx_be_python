from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_future

def main():
    display_current_datetime()
    add_days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(add_days)
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()
