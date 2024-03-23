# Take input from user
n = int(input("Enter the number of processes: "))
burst_time = list(map(int, input("Enter the burst time for each process separated by space: ").split()))

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
    # Find the process with the shortest remaining time
    min_time = float('inf')
    min_index = None
    for i in range(n):
        if remaining_time[i] > 0 and remaining_time[i] < min_time:
            min_time = remaining_time[i]
            min_index = i
    
    # If no process found, break the loop
    if min_index is None:
        break
    
    # If a process is executing, update its remaining time, waiting time, and completion time
    if executing:
        remaining_time[executing] -= 1
        if remaining_time[executing] == 0:
            completion_time[executing] = current_time + 1
            executing = False
    
    # If a process is not executing, set it as executing and update its waiting time
    if not executing:
        executing = min_index
        waiting_time[executing] = current_time - completion_time[executing]
    
    # Increment current time
    current_time += 1

# Calculate turnaround time for each process
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

# Print output in table form
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{i+1}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
# Calculate average waiting time and turnaround time
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n

# Print average waiting time and turnaround time
print(f"\nAverage Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")
