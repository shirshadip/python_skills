queue = []

def enqueued(item):
    queue.append(item)

def dequeued():
    if queue:
        return queue.pop(0)
    return None

def peek():
    if queue:
        return queue[0]
    return None


enqueued(1)
enqueued(2)
print(dequeued())  # Output: 1
print(peek())      # Output: 2
print("is not a palindrome")    
print (queue)