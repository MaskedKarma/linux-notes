# A simple to-do list.
import time


tasks = []
attempts = 0


def invalid_choice(x):
    try:
        return int(x)
    except ValueError:
        return None

def check_attempts(attempts):
    attempts += 1
    time.sleep(1)
    if attempts >= 5:
        print("Too many invalid attempts. Goodbye!")
        exit()
    return attempts

def option_length(y):
    return 0 <= y < len(tasks)


while True:
    print("------------------------------------------------------------------------------------------------------")
    print()
    print("To-Do list.")
    print()
    print()
    print("Would you like to add a task (1), remove a task (2), view current tasks (3), mark a task as complete (4), or quit (5)?")
    print()
    choice = input()
    result = invalid_choice(choice)
    if result is None:
        print("Sorry, please put in a number!")
        attempts = check_attempts(attempts)
        continue
    choice = result
    attempts = 0
    if choice == 1:
        print("What task would you like to add?")
        tasks_add = input()
        tasks.append(tasks_add)
    elif choice == 2:
        while True:
            print("What task would you like to remove?")
            for i, task in enumerate(tasks):
                print(f"{i}  {task}")
            print("Please choose the index assigned to your task.")
            tasks_remove_input = input()
            result_r = invalid_choice(tasks_remove_input)
            if result_r is None:
                    print("Sorry, please put in a number!")
                    print()
                    print()
                    attempts = check_attempts(attempts)
                    continue
            tasks_remove = int(result_r)
            if option_length(tasks_remove):
                print(f"Are you sure {tasks[tasks_remove]} is the correct task?")
            else:
                print("That number isn't on the list!")
                print()
                print()
                continue
            print("1 for yes | 2 for no")
            print()
            print()
            print()
            answer = input()
            result_agree = invalid_choice(answer)
            if result_agree is None:
                print("Sorry, please put in a number!")
                print()
                print()
                attempts = check_attempts(attempts)
                continue
            if answer == '1':
                tasks.pop(tasks_remove)
                break
            elif answer == '2':
                print("No worries. Nothing was deleted.")
                print()
                print()
    elif choice == 3:
        print()
        print()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    elif choice == 4:
        while True:
            for i, task in enumerate(tasks):
                print(f"{i} {task}")
            print("Which task have you finished?")
            complete_input = input()
            complete = invalid_choice(complete_input)
            if complete is None:
                print("Sorry, please put in a number!")
                print()
                print()
                attempts = check_attempts(attempts)
                continue
            if option_length(complete):
                tasks[complete] = f"{tasks[complete]} completed."
                break
            else:
                print("That number isn't on the list!")
                print()
                print()
                continue
    elif choice == 5:
        print()
        print()
        print("Thank you using our services!")
        break