def sort_tasks(tasks):
    tasks_queue = []
    mapper = {}  # {priority: task} {5: time_alloted}
    tasks = sorted(tasks, reverse=True)  # Inital reverse sorted list
    print(tasks)
    for i in tasks:
        # insert in queue
        # If a value exists in tasks_queue, pop that element, check if the priority matches and time     alloted >
        if not tasks_queue:  # If the task queue is empty
            tasks_queue.append(i)
        else:
            top_task = tasks_queue[-1]
            if top_task[0] == i[0]:  # Matching priority
                tasks_queue.pop(-1)
                if top_task[1] > i[1]:  # Checking the time
                    tasks_queue.append(i)
                    tasks_queue.append(top_task)
                else:
                    tasks_queue.append(top_task)
                    tasks_queue.append(i)
            else:
                tasks_queue.append(i)
    return tasks_queue


tasks = [[5, 3],[5,1],[4, 2], [3, 1]]
my_task  = sort_tasks(tasks)
print(my_task)
#print(sorted(tasks, reverse=True))
