import threading
import queue
import time

# Define a shared queue with maximum size of 10 items
shared_queue = queue.Queue(maxsize=10)

# Define a producer function to add items to shared queue
def producer():
    for i in range(20):
        shared_queue.put(i)
        print(f"Producer added item {i} to shared queue")
        time.sleep(3)

# Define a consumer function to remove items from shared queue
def consumer():
    while True:
        try:
            item = shared_queue.get(block=False)
            print(f"Consumer removed item {item} from shared queue")
        except queue.Empty:
            pass
        time.sleep(1)

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start both threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()
