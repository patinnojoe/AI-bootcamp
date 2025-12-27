""" CREATE A FUNCTION, THAT CREATES A TASK, UPDATES THE TASK, DELETE THE TASK, SHOW ALL TASKS """

tasks =[]
next_id = 1


def create_new_task():
    global next_id
    task_name = input(f"Enter the name of your task: ")
    task_content = input(f"Enter the task you want to perform: ")
   
    tasks.append({
        "name": task_name,
        "task": task_content,
        "task_id": next_id,
        "status": "Incomplete"
    })
    next_id += 1
    return tasks



def mark_as_complete():
    try:
        task_id = int(input(f"Enter task id: "))
        for task in tasks:
            if task['task_id'] == task_id:
              task['status'] = "Completed"
              return "Task status completed"
          
        print(tasks)
        
    except Exception as e:
        return e

def print_all_task():
    if len(tasks) < 1:
        print("No task added yet")
    for task in tasks:
        print(f"\n  task_id: { task['task_id']} title: {task['name']} content: {task['task']} status: {task['status']} ")

def delete_task():
    try:
        task_id = int(input(f"Enter the task id: "))
        for index, task in enumerate(tasks):
            if task['task_id'] == task_id:
                del task[index]
                break
        return "Task deleted"
    except Exception as e:
        return e
    
    
            
while True:
    print(f"\n 1. Create Task \n 2. Mark Task as Complete \n 3. Edit Task \n 4. View all Tasks \n 5. Delete Tasks \n 6. Exit ")
    
    try:
        choice = int(input(f"Please select an option: "))
        if(choice == 1):
            create_new_task()
        elif choice ==2:
            mark_as_complete()
        elif choice == 3:
            print("edit logic")
        elif choice == 4:
            print_all_task()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            break
    except Exception as e:
        print(e)
   

