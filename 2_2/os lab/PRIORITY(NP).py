# Take input from user
n = int(input("Enter the number of processes: "))
burst_time = list(map(int, input("Enter the burst time for each process separated by space: ").split()))
priority = list(map(int, input("Enter the priority for each process separated by space: ").split()))

# Initialize waiting time, turnaround time, and completion time arrays with 0
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n

# Create a list of tuples for each process with index, burst time, and priority
processes = [(i, burst_time[i], priority[i]) for i in range(n)]

# Sort the list of processes by priority
processes.sort(key=lambda x: x[2])

# Initialize current time to 0
current_time = 0

# Loop through each process and update waiting time, completion time, and current time
for i in range(n):
    process = processes[i]
    process_index = process[0]
    process_burst_time = process[1]
    process_priority = process[2]
    
    waiting_time[process_index] = current_time
    completion_time[process_index] = current_time + process_burst_time
    turnaround_time[process_index] = completion_time[process_index] - waiting_time[process_index]
    
    current_time = completion_time[process_index]

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
