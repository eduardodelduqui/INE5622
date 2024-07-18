class ParsingStack:
  def __init__(self, start) -> None:
    self.__stack = ['$', start]

  def push(self, value: list):
    self.__stack = self.__stack + value[::-1]

  def pop(self):
    return self.__stack.pop()
    
  def get_top(self) -> str:
    return self.__stack[-1]
    
  def get_stack(self):
    return self.__stack
  
  def is_empty(self):
    return len(self.__stack) == 1 and self.__stack[0] == '$'

  
