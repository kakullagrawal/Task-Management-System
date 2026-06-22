tasks =[]

def load_task():
    try:
        with open("tasks.txt","r") as file:
            for line in file:
                task,done = line.strip().split(",")
                tasks.append({"task": task, "done": False})
    except FileNotFoundError:
        pass
    
def save_task():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task'], task['done']}\n")



def add_task():
    task = input("add task:")
    tasks.append({
        "task": task,
        "done": False
    })
    save_task()
    print("task added!")

def view_task():
    if not tasks:
        print("no tasks found!")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - Done: {task['done']}")

def mark_task():
    view_task()
    task_no = int(input("which task you want to mark: "))
    index= task_no - 1
    if 0<= index <=len(tasks):
        tasks[index]["done"] = True
    else:
        print("invalid input!")
    save_task()

def delete_task():
    view_task()
    try:
        remove = int(input("which task you want to remove"))
        index= remove -1
        if 0 <= index <= len(tasks):
            tasks.pop(index)
            save_task()
            print("deleted!")
        else:
            print("no task as such!")
    except ValueError:
        print("input is not valid")

load_task()

while True:
    print("\n1.add task")
    print("2.view task")
    print("3.mark as done")
    print("4.delete task")
    print("5.exit")

    choice = int(input("enter a number: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        break
    else:
        print("invalid input:")