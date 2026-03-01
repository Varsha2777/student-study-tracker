import datetime
assignments = []
study_log = []
def add_assignment():
    title = input("Enter assignment title: ")
    subject = input("Enter subject: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    assignments.append({
        "title": title,
        "subject": subject,
        "due_date": due_date,
        "completed": False
    })
    print(" Assignment added successfully!")
def view_assignments():
    if not assignments:
        print("No assignments added yet.")
        return
    print("\n Your Assignments:")
    today = datetime.date.today()
    for i, task in enumerate(assignments):
        due = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        status = " Completed" if task["completed"] else " Pending"
        days_left = (due - today).days
        print(f"{i+1}. {task['title']} ({task['subject']})")
        print(f"   Due: {task['due_date']} | Days left: {days_left} | Status: {status}")
        if days_left <= 2 and not task["completed"]:
            print("   Deadline approaching!")
def mark_completed():
    view_assignments()
    try:
        choice = int(input("Enter assignment number to mark as completed: "))
        assignments[choice - 1]["completed"] = True
        print(" Assignment marked as completed!")
    except:
        print("Invalid choice.")
def log_study_hours():
    hours = float(input("Enter number of study hours today: "))
    date = str(datetime.date.today())
    study_log.append({"date": date, "hours": hours})
    print(" Study hours logged!")
def view_study_summary():
    total = sum(entry["hours"] for entry in study_log)
    print(f"\nTotal Study Hours: {total}")
def main():
    while True:
        print("\n==== Student Study Tracker ====")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Assignment Completed")
        print("4. Log Study Hours")
        print("5. View Study Summary")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            log_study_hours()
        elif choice == "5":
            view_study_summary()
        elif choice == "6":
            print("Good luck with your studies! 🎓")
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main
