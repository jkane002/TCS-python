# Stack Element Reversal
# Given a stack of elements, reverse the order of the elements.
# assume Queue() gives you the entire queue

def reverse(stack):
    tempQueue = Queue()
    while not stack.isEmpty():
        tempQueue.enqueue(stack.pop())
    while not tempQueue.isEmpty():
        stack.push(tempQueue.dequeue())
