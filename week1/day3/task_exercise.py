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
        
    except Exception as e:
        print(e)
            
            
        


print(mark_as_complete())
   

