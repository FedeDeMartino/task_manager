from services.task_manager import TaskManager

def get_priority():
    while True:
        priority = input("Enter task priority (1: Low, 2: Medium, 3: High): ")
        if priority in ["1", "2", "3"]:
            return priority
        print("Invalid priority. Please enter 1, 2, or 3.")

def main():

    task_manager = TaskManager()
    task_manager.load()

    while True:
        print("\nTasks:\n")

        choice = input(
            "Press [a] to add task,\n"
            "[c] to complete task,\n"
            "[l] to list all tasks,\n"
            "[d] to destroy all tasks,\n"
            "[e] to edit task,\n"
            "[q] to quit:\n"
        ).lower()

        if choice == "a":
            task_name = input("Enter task name: ").strip()
            task_priority = get_priority()
            task_manager.add(task_name, task_priority)
        elif choice == "c":
            task_manager.list_tasks()
            try:
                task_number = int(input("Enter task number to complete: "))
                task_manager.complete(task_number)
                task_manager.save()
            except ValueError:
                print("Invalid task number. Please enter a valid integer.")
        elif choice == "l":
            task_manager.list_tasks()
        elif choice == "d":
            confirm = input("Are you sure you want to destroy all tasks? (y/n): ").lower()
            if confirm == 'y':
                task_manager.remove_all()
                print("All tasks have been destroyed.")
        elif choice == "e":
            task_manager.list_tasks()
            try:
                task_number = int(input("Enter task number to edit: "))
                new_name = input("Enter new task name: ").strip()
                new_priority = get_priority()
                task_manager.edit(task_number, new_name, new_priority)
                task_manager.save()
            except ValueError:
                print("Invalid task number. Please enter a valid integer.")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
