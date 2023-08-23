import pickle

def save_tasks(tasks):
    with open('tasks.pickle', 'wb') as f:
        pickle.dump(tasks, f)

def load_tasks():
    try:
        with open('tasks.pickle', 'rb') as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def main():
    tasks = load_tasks()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task: ")
            tasks.append({'task_name': task_name, 'completed': False})
        elif choice == '2':
            for i, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i+1}. {task['task_name']} - {status}")
        elif choice == '3':
            index = int(input("Enter task index to mark as complete: "))
            tasks[index - 1]['completed'] = True
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            del tasks[index - 1]
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
