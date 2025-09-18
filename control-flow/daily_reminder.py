task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task}' is a high priority task that requires immediate attention today!")
        else:
            if time_bound == "no":
                print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task. Try to complete it within the next couple of days.")
        else:
            if time_bound == "no":
                print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.") 
        else:
            if time_bound == "no":
                print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")    