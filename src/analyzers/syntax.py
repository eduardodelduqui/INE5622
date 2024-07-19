from utils.parsing_table import ParsingTable
from utils.parsing_stack import ParsingStack

class SyntaxAnalyzer:
  def __init__(self) -> None:
    self.parsing_table = ParsingTable()
    self.parsing_stack = ParsingStack("A")
    self.string = ''
    self.string_position = 0
    

  def print_stack(self):
    print(self.parsing_stack.get_stack())

  def process(self, string):
    self.string = string + '$'
    # print(self.string)
    while not self.parsing_stack.is_empty():
      parsing_stack_top = self.parsing_stack.get_top()
      print(parsing_stack_top)
      print("linha22")
      if parsing_stack_top.isupper():
        self.parsing_stack.pop()
        production = self.parsing_table.get_production(parsing_stack_top, self.string[self.string_position])
        self.parsing_stack.push(production)
        # print(production)
        print('linha28')
      else:
        print("linha30")
        if parsing_stack_top == self.string[self.string_position]:
          self.parsing_stack.pop()
          self.string_position += 1
        elif parsing_stack_top == 'λ':
          self.parsing_stack.pop()
        else:
          print('Error: Expected', parsing_stack_top, 'but found', self.string[self.string_position])
          break
