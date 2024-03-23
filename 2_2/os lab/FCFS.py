# Take input from user
n = int(input("Enter the number of processes: "))
burst_time = list(map(int, input("Enter the burst time for each process separated by space: ").split()))

# Initialize waiting time, turnaround time, and completion time arrays with 0
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n

# Initialize current time to 0
current_time = 0

# Loop through each process and update waiting time, completion time, and current time
for i in range(n):
    completion_time[i] = current_time + burst_time[i]
    turnaround_time[i] = completion_time[i] - current_time
    waiting_time[i] = turnaround_time[i] - burst_time[i]
    current_time = completion_time[i]

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
