import threading
import time

# Number of philosophers at the table
NUM_PHILOSOPHERS = 5

class DiningPhilosophers:
    def __init__(self):
        self.chopsticks = [threading.Condition() for i in range(NUM_PHILOSOPHERS)]
    
    def pick_left_chopstick(self, philosopher_id):
        self.chopsticks[philosopher_id].acquire()

    def pick_right_chopstick(self, philosopher_id):
        self.chopsticks[(philosopher_id + 1) % NUM_PHILOSOPHERS].acquire()

    def put_left_chopstick(self, philosopher_id):
        self.chopsticks[philosopher_id].notify()
        self.chopsticks[philosopher_id].release()

    def put_right_chopstick(self, philosopher_id):
        self.chopsticks[(philosopher_id + 1) % NUM_PHILOSOPHERS].notify()
        self.chopsticks[(philosopher_id + 1) % NUM_PHILOSOPHERS].release()

    def philosopher(self, philosopher_id):
        while True:
            # Think
            print("Philosopher {} is thinking...".format(philosopher_id))
            time.sleep(1)

            # Pick up chopsticks
            self.pick_left_chopstick(philosopher_id)
            self.pick_right_chopstick(philosopher_id)

            # Eat
            print("Philosopher {} is eating...".format(philosopher_id))
            time.sleep(2)

            # Put down chopsticks
            self.put_left_chopstick(philosopher_id)
            self.put_right_chopstick(philosopher_id)

dining_philosophers = DiningPhilosophers()
threads = []
for i in range(NUM_PHILOSOPHERS):
    threads.append(threading.Thread(target=dining_philosophers.philosopher, args=(i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Dinner is over!")
