class Stack():

    #Constructor
    def __init__(self,list):
      # __ means private (our __stack attribute is private)
      self.__stack = []
      for value in list:
        self.__stack.append(value)
        
    def push(self,value):
      print(" < PUSH < " + str(value))
      self.__stack.append(value)
      
    def pop(self):
      if len(self.__stack)>0:
        index = len(self.__stack) - 1
        print(" > POP > " + str(self.__stack[index]))
        return self.__stack.pop(index) #pop() Returns the value of the item that has been removed
      else:
        print("Stack is empty.")
        return False
      
    def output(self):
      st = ""
      for value in self.__stack:
        st = st + " > " + str(value) 
      print(st)  
      
