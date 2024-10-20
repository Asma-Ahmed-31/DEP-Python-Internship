import csv

# Function to set the file name dynamically
def set_filename():
    global FILENAME
    file_name_input = input("Enter the filename (including .csv extension) or press Enter to use the default 'Programs-tasks.csv': ")
    if file_name_input:
        FILENAME = file_name_input
    else:
        FILENAME = "Programs-tasks.csv"
    print(f"Using file: {FILENAME}")

def load_tasks():
    tasks = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['ID'] = int(row['ID'])
                tasks.append(row)
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Description', 'Status'])
            writer.writeheader()
    return tasks

def save_tasks(tasks):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Description', 'Status'])
        writer.writeheader()
        writer.writerows(tasks)

def add_task(tasks):
    task_id = len(tasks) + 1
    description = input("Enter the task description: ")
    tasks.append({'ID': task_id, 'Description': description, 'Status': 'Pending'})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if tasks:
        for task in tasks:
            print(f"[ID: {task['ID']}] {task['Description']} - Status: {task['Status']}")
    else:
        print("No tasks available.")

def remove_task(tasks):
    task_id = int(input("Enter task ID to remove: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Task not found.")

def mark_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        task['Status'] = 'Completed'
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Task not found.")

def edit_task(tasks):
    task_id = int(input("Enter task ID to edit: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        new_desc = input("Enter new description: ")
        task['Description'] = new_desc
        save_tasks(tasks)
        print("Task description updated.")
    else:
        print("Task not found.")

def search_task(tasks):
    keyword = input("Enter a keyword to search tasks: ").lower()
    found_tasks = [task for task in tasks if keyword in task['Description'].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"[ID: {task['ID']}] {task['Description']} - Status: {task['Status']}")
    else:
        print("No matching tasks found.")

def filter_tasks(tasks):
    status = input("Filter tasks by status (Pending/Completed): ").capitalize()
    filtered_tasks = [task for task in tasks if task['Status'] == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"[ID: {task['ID']}] {task['Description']} - Status: {task['Status']}")
    else:
        print(f"No tasks with status '{status}'.")

def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Operation canceled.")

def sort_tasks(tasks):
    sort_by = input("Sort tasks by (1) ID or (2) Status: ")
    if sort_by == '1':
        tasks.sort(key=lambda x: x['ID'])
    elif sort_by == '2':
        tasks.sort(key=lambda x: x['Status'])
    else:
        print("Invalid choice.")
    save_tasks(tasks)
    print("Tasks sorted.")

# Menu function
def menu():
    set_filename()  # Ask for filename at the start
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            search_task(tasks)
        elif choice == '7':
            filter_tasks(tasks)
        elif choice == '8':
            clear_all_tasks(tasks)
        elif choice == '9':
            sort_tasks(tasks)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

# Call the menu function directly
menu()