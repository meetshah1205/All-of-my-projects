# To-Do List App
todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
    else:
        print("Task not found in the to-do list.")

# Main application loop
while True:
    print("To-Do List:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")
    print("Options:")
    print("Type 'add' to add a task")
    print("Type 'remove' to remove a task")
    print("Type 'quit' to exit the program")
    user_input = input(": ")

    if user_input == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "remove":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif user_input == "quit":
        break
    else:
        print("Unknown input")

