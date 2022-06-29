# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")




# Tasks = List of tasks which need to be priorititizdd
# N Total alloted/available time

# requirement would be to schedule high priority tasks first
# Reject a task only if its required time is > than available time

# Input
# tasks = [[1, 4]] 1 would be priority, 4 would be the time required to complete a task
# (1 would be lowest, 5 would be highest)

# Output would be list of tasks which can be completed in the alloted time(10)


"""
1. Sorting the tasks as per the priority
2. traverse from highest to lowest
3. Cumulative running count of time consumed
  while time_consumed <=time_alloted
   If the time of the task > available time:
    continue
   add to the result list
4: If the priorities are same , check for the time consumed part, if the time of task is lower, schedule that first

tasks = [[5, 3][4, 2], [3, 1]]
total_alloted = 5

time_consumed = 0, available_time = 5
5, 3
result = [[5, 3]]
task_Counter = 0
if 3 < 5:
    result = [[5, 3]]

task_counter = 1
if
"""

def schedule_tasks(tasks, available_time):
    sorted_tasks = sort_tasks(tasks)  # sorted list of tasks
    time_consumed = 0
    task_counter = 0
    result = []
    if not tasks:
        return []

    while time_consumed < available_time:
        task_priority, task_time_needed = sorted_tasks[task_counter][0], sorted_tasks[task_counter][1]
        if task_time_needed < available_time:
            result.append(sorted_tasks[task_counter])
            time_consumed += task_time_needed
        task_counter += 1
    return result


def sort_tasks(tasks):
    tasks_queue = []
    mapper = {}  # {priority: task} {5: time_alloted}
    tasks = sorted(tasks, reverse=True)  # Inital reverse sorted list
    for i in tasks:
        # insert in queue
        # If a value exists in tasks_queue, pop that element, check if the priority matches and time     alloted >
        if not tasks_queue:  # If the task queue is empty
            tasks_queue.append(i)
        else:
            top_task = tasks_queue[-1]
            if top_task[0] == i[0]:  # Matching priority
                if top_task[1] > i[1]:  # Checking the time
                    tasks_queue.append(i)
                    tasks_queue.append(top_task)
                else:
                    tasks_queue.append(top_task)
                    tasks_queue.append(i)
    return tasks_queue





"""""
2: 
"""

class MaxBinary:
    def __init__(self):
        self.traverse_range = 2147483647


def get_min_max_binary_counts(self, num: int) -> list:
    results = []
    if not num:
        return []

    input_ones = self.get_ones(str(num))  # Input's total number of 1s

    results.append(self.get_max_binary(num, input_ones))
    results.append(self.get_min_binary(num, input_ones))
    return results


def get_ones(self, num: str) -> int:
    cnt = 0
    for i in range(len(num)):
        if num[i] == "1":
            cnt += 1
    return cnt


def get_max_binary(self, num, input_ones):
    for i in range(num, self.traverse_range, 1):
        max_ones = self.get_ones(bin(i)[2::])  # 1
        if max_ones == input_ones:  # 1==1
            return i  # 4
    return -1


def get_min_binary(self, num, input_ones):
    for i in range(num, 1, -1):  # 2-> 1
        max_ones = self.get_ones(bin(i)[2::])  # 1
        if max_ones == input_ones:  # 1==1
            return i  #
    return -1


"""
2147483647
1.1 
"abc"
"""

# Pre-cache the count of 1s in hashmap {1:1, 2:1, 3:2 ....}
# Hash Map(2147483647), results,
"""
"""

