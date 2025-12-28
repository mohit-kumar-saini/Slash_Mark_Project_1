FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append([task, status])
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task[0] + "|" + task[1] + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nTo-Do List:")
        for i in range(len(tasks)):
            status = "Done" if tasks[i][1] == "1" else "Not Done"
            print(f"{i+1}. {tasks[i][0]} ({status})")
        print()

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append([task_name, "0"])
    save_tasks(tasks)
    print("Task added successfully.\n")

def mark_completed(tasks):
    display_tasks(tasks)
    num = int(input("Enter task number to mark completed: "))
    if 1 <= num <= len(tasks):
        tasks[num-1][1] = "1"
        save_tasks(tasks)
        print("Task marked as completed.\n")
    else:
        print("Invalid task number.\n")

def remove_task(tasks):
    display_tasks(tasks)
    num = int(input("Enter task number to remove: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task removed successfully.\n")
    else:
        print("Invalid task number.\n")

tasks = load_tasks()

while True:
    print("==== To-Do List Menu ====")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        mark_completed(tasks)
    elif choice == "4":
        remove_task(tasks)
    elif choice == "5":
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Try again.\n")
