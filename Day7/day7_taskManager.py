import os

FILE_NAME="task.txt"


def load_task():
    tasks={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id,title,status=line.strip().split(" | ")
                tasks[int(task_id)]={"title":title,"status":status}
    return tasks

#save task to file
def save_task(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

 #add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added with ID {task_id}")

def view_tasks(tasks):
    if not tasks:
        print("No task available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


def mark_task_colplete(tasks):
    task_id=int(input("enter task id to marks as complete: ")   )
    if task_id in tasks:
        tasks[task_id]["status"]="Completed"
        print(f"Task {tasks[task_id]['title']} marked as complete")
    else:
        print("Task ID not found")


def delete_task(tasks):
    task_id=int(input("enter task ID to Delete: ")   )
    if task_id in tasks:
        deleted_task=tasks.pop(task_id)
        print(f"Task {deleted_task['title']} has been Deleted")
    else:
        print("Task ID not found")


def main():
    tasks=load_task()
    while True:
        print("\n Task manage Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice=input("Enter your coice:"
                     )
        if(choice=="1"):
            add_task(tasks)
        elif(choice=="2"):
            view_tasks(tasks)
        elif(choice=="3"):
            mark_task_colplete(tasks)
        elif(choice=="4"):
            delete_task(tasks)
        elif(choice=="5"):
            save_task(tasks)
            print("Good Bye")
            break;
        else:
            print("Option not avaialble")


main()





