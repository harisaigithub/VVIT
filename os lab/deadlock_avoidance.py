# Initialize available resources
available = [int(x) for x in input("Enter the number of available resources: ").split()]

# Initialize maximum resources required by each process
max_req = []
n_processes = int(input("Enter the number of processes: "))
for i in range(n_processes):
    req = [int(x) for x in input(f"Enter the maximum resources required by process {i}: ").split()]
    max_req.append(req)

# Initialize resources allocated to each process
alloc = []
for i in range(n_processes):
    a = [int(x) for x in input(f"Enter the resources allocated to process {i}: ").split()]
    alloc.append(a)

# Initialize need matrix
need = []
for i in range(n_processes):
    n = [max_req[i][j] - alloc[i][j] for j in range(len(available))]
    need.append(n)

# Initialize the work and finish arrays
work = available[:]
finish = [False] * n_processes

# Start the deadlock avoidance algorithm
while True:
    # Check for an unfinished process with need <= work
    found = False
    for i in range(n_processes):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
            found = True
            break
    
    if not found:
        # No process found that can be finished
        if all(finish):
            # All processes are finished, so there is no deadlock
            print("No deadlock.")
        else:
            # Some processes are unfinished, so there is a deadlock
            print("Deadlock detected.")
        break
    
    # Finish the process and release its resources
    for j in range(len(available)):
        work[j] += alloc[i][j]
    finish[i] = True
