#!/bin/bash

task = input("Enter task: ")
task_priority = input("Enter task priority: (high,medium,low) ")
time_bound = input("Is task time bond: (yes or no) ")


match task_priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Step 3: Check if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Step 4: Provide a customized reminder
print(reminder)
