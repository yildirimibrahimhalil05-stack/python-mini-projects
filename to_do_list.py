to_do_list = []

while True:
    print("1. Add a task\n2. Show tasks\n3. Delete a task\n4. Exit\n5. Mark which is done")
    selection = input()

    if selection == "1":
        given_task = input("Enter a new task:").strip()
        given_task_1 = "[ ] " + given_task
        if given_task_1 in to_do_list:
            print("Already in tasks")
        elif given_task == "":
            print("Task cannot be empty")
        else:
            to_do_list.append(given_task_1)
            print("Task added successfully")
        continue

    elif selection == "2":
        if not to_do_list:
            print("Nothing to do")
            continue
        else:
            for number, task in enumerate(to_do_list, start=1):
                print(f"{number}) {task}")
        continue

    elif selection == "3":
        if not to_do_list:
            print("There are no tasks to delete.")
            continue
        for number, task in enumerate(to_do_list, start=1):
            print(f"{number}. {task}")
        while True: # We are waiting for user to give a valid number
            try:
                deleted_task = int(input("Please enter a task number to delete: "))
                if len(to_do_list) < deleted_task or deleted_task < 1:
                    print("Please enter a valid task number")
                else:
                    to_do_list.pop(deleted_task - 1)
                    print("Task deleted successfully")
                    break

            except ValueError:
                print("Enter a valid number.")

        continue

    elif selection == "4":
        count = 0
        for task in to_do_list:
            if task.startswith("[ ]"):
                count += 1
        print(f"Goodbye! You have {count} tasks remaining")
        break
    elif selection == "5":
        if not to_do_list:
            print("Nothing to do")
            continue
        while True:
            try:
                for number, task in enumerate(to_do_list, start=1):
                    print(f"{number}) {task}")
                done = int(input("Please enter a task number to mark as done: "))
                if len(to_do_list) < done or done < 1:
                    print("Please enter a valid task number")
                else:
                    selected_task = to_do_list[done - 1]

                    if selected_task.startswith("[✓]"):
                        print("This task is already completed")
                    else:
                        to_do_list[done - 1] = selected_task.replace("[ ] ", "[✓] ", 1)
                        print("The given task was marked as done")
                    break

            except ValueError:
                print("Enter a valid number")

    else:
        print("Enter a valid number.")
        continue
