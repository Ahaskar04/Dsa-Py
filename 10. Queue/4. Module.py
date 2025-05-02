# Python Collection Module
# How to use collections.deque() to create a queue

from collections import deque
customer_queue = deque(maxlen=5)  # maxlen is the maximum size of the queue
customer_queue.append('Customer 1')
customer_queue.append('Customer 2')
print(customer_queue) 
print(customer_queue.popleft())  # Remove the first customer
print(customer_queue.clear())  # Clear the queue

# Python Queue Module

import queue as q
customer_queue = q.Queue(maxsize=5)  # maxsize is the maximum size of the queue
print(customer_queue.empty())  # Check if the queue is empty
print(customer_queue.qsize())  # Get the size of the queue
customer_queue.put('Customer 1')  # Add a customer to the queue
customer_queue.put('Customer 2')  # Add another customer to the queue
print(customer_queue.get())  # Remove the first customer

# Python Multiprocessing Queue(very similar to queue.Queue)
# This is used for inter-process communication

from multiprocessing import Queue
customer_queue = Queue(maxsize=5)  # maxsize is the maximum size of the queue
print(customer_queue.empty())  # Check if the queue is empty
print(customer_queue.qsize())  # Get the size of the queue
customer_queue.put('Customer 1')  # Add a customer to the queue
customer_queue.put('Customer 2')  # Add another customer to the queue
print(customer_queue.get())  # Remove the first customer