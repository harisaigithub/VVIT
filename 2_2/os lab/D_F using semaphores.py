import threading

# Number of philosophers at the table
NUM_PHILOSOPHERS = 5

# List of semaphores for chopsticks (one semaphore per chopstick)
chopsticks = [threading.Semaphore(1) for i in range(NUM_PHILOSOPHERS)]

def philosopher(id):
    left_chopstick = id
    right_chopstick = (id + 1) % NUM_PHILOSOPHERS

    while True:
        # Think
        print("Philosopher {} is thinking...".format(id))

        # Pick up chopsticks
        chopsticks[left_chopstick].acquire()
        chopsticks[right_chopstick].acquire()

        # Eat
        print("Philosopher {} is eating...".format(id))

        # Put down chopsticks
        chopsticks[left_chopstick].release()
        chopsticks[right_chopstick].release()

threads = []
for i in range(NUM_PHILOSOPHERS):
    threads.append(threading.Thread(target=philosopher, args=(i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Dinner is over!")
