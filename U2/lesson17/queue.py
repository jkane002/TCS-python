class Queue():

    #Constructor
    def __init__(self,list):
      # __ means private (our __queue attribute is private)
      self.__queue = []
      for value in list:
        self.__queue.append(value)
        
    def enqueue(self,value):
      print(" < Enqueue < " + str(value))
      self.__queue.append(value)
      
    def dequeue(self):
      if len(self.__queue)>0:
        print(" > Dequeue > " + str(self.__queue[0]))
        return self.__queue.pop(0) #pop() Returns the value of the item that has been removed
      else:
        print("Queue is empty.")
        return False
      
    def output(self):
      st = ""
      for value in self.__queue:
        st = st + " > " + str(value) 
      print(st)  
      
