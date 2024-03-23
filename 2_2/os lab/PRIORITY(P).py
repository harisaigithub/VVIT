# Take input from user
n = int(input("Enter the number of processes: "))
burst_time = list(map(int, input("Enter the burst time for each process separated by space: ").split()))
priority = list(map(int, input("Enter the priority for each process separated by space: ").split()))

# Initialize waiting time, turnaround time, remaining time, and completion time arrays with 0
waiting_time = [0] * n
turnaround_time = [0] * n
remaining_time = burst_time.copy()
completion_time = [0] * n

# Set current time and flag to check if a process is executing or not
current_time = 0
executing = False

# Loop until all processes are completed
while True:
    # Find the process with the highest priority
    max_priority = float('-inf')
    max_index = None
    for i in range(n):
        if remaining_time[i] > 0 and priority[i] > max_priority:
            max_priority = priority[i]
            max_index = i
    
    # If no process found, break the loop
    if max_index is None:
        break
    
    # If a process is executing, update its remaining time, waiting time, and completion time
    if executing:
        remaining_time[executing] -= 1
        if remaining_time[executing] == 0:
            completion_time[executing] = current_time + 1
            executing = False
    
    # If a process is not executing or a higher priority process is found, set the new process as executing and update its waiting time
    if not executing or max_priority > priority[executing]:
        if executing:
            waiting_time[executing] = current_time - completion_time[executing]
        executing = max_index
    
    # Increment current time
    current_time += 1

# Calculate turnaround time for each process
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

# Print output in table form
print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{i+1}\t{burst_time[i]}\t\t{priority[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
# Calculate average waiting time and turnaround time
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n

# Print average waiting time and turnaround time
print(f"\nAverage Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")
