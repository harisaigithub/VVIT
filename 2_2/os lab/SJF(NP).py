# Take input from user
n = int(input("Enter the number of processes: "))
burst_time = list(map(int, input("Enter the burst time for each process separated by space: ").split()))

# Initialize waiting time and turnaround time arrays with 0
waiting_time = [0] * n
turnaround_time = [0] * n

# Sort processes based on burst time
sorted_processes = sorted(range(n), key=lambda i: burst_time[i])

# Calculate waiting time and turnaround time for each process
for i in range(n):
    if i == 0:
        waiting_time[sorted_processes[i]] = 0
    else:
        waiting_time[sorted_processes[i]] = burst_time[sorted_processes[i-1]] + waiting_time[sorted_processes[i-1]]
    turnaround_time[sorted_processes[i]] = waiting_time[sorted_processes[i]] + burst_time[sorted_processes[i]]

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
