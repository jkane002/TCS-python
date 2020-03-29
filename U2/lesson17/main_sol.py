#Stacks and Queues - www.101computing.net/stacks-and-queues-using-python/
from stack import Stack
from queue import Queue

print("> > > > > Stack > > > > >")
print("")
myStack = Stack(["Mia","Eshan","Simon","Zhang","Sophia","Tom"])


myStack.output()
print("")

myStack.pop()

myStack.pop()

myStack.push("Ilona")

print("")
myStack.output()
print("")
print("")

print("> > > > > Queue > > > > >")
print("")

myQueue = Queue(["Mia","Eshan","Simon","Zhang","Sophia","Tom"])


myQueue.output()
print("")

myQueue.dequeue()

myQueue.dequeue()

myQueue.enqueue("Ilona")

print("")
myQueue.output()
print("")
