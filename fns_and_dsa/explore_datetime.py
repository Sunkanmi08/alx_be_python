from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0)
    print(f"current date and time: {current_date}")

def calculate_future_date(date):
    future_date = timedelta(days=date) + datetime.now()
    
    return future_date




def main():
    display_current_datetime()
    add_date = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(add_date)
    print(f"Future date: {future_date.replace(microsecond=0)}")
 

main()



def display_current_datetime():
    current_date = datetime.datetime.now().replace(microsecond=0)
    print(f"current date and time: {current_date}")
