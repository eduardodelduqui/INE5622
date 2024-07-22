class ParsingStack:
  def __init__(self, start) -> None:
    self.stack = ['$', start]

  def push(self, value: str):
    for s in reversed(value):
      self.stack.append(s)
    # print(self.stack)
    

  def pop(self):
    return self.stack.pop()
    
  def get_top(self) -> str:
    return self.stack[-1]
    
  
  def is_empty(self):
    return len(self.stack) == 0

  
