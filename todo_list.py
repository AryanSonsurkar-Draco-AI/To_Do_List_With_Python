def new_task(task):
    with open("tasks.txt", "a") as file:
        file.write(f"[ ] {task}\n")


def read_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")


def mark_task(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    if "[✔]" in tasks[task_number - 1]:
        print("Task is already marked as done.")
        return

    tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[✔]")

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)


def remove_task(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    tasks.pop(task_number - 1)

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)


def todo():
    while True:
        print("\n---------------------------")
        print("Welcome to To Do List Manager")
        print("-----------------------------")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Exiting the To Do List Manager! Goodbye")
            break

        elif choice == "1":
            task = input("Enter task: ").strip()
            if task:
                new_task(task)
                print("Task added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            read_task()

        elif choice == "3":
            read_task()
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_task(num)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            read_task()
            try:
                num = int(input("Enter task number to remove: "))
                remove_task(num)
            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    todo()
