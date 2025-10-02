# daily_reminder.py

while True:
    # Step 1: Ask for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Step 2: Use match case for priority
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Note: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority"

    # Step 3: Add time sensitivity check
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Step 4: Print final reminder
    print(message)

    # Step 5: Ask if user wants another reminder
    again = input("Do you want to enter another task? (yes/no): ")
    if again.lower() != "yes":
        break
