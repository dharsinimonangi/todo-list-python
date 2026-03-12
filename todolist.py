tasks = []
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except:
    pass
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(i, t)

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)

    elif choice == "4":
        break

    else:
        print("Invalid choice")

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")