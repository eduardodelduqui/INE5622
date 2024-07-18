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
    self.string = string

    while not self.parsing_stack.is_empty():
      parsing_stack_top = self.parsing_stack.get_top()
      if parsing_stack_top.isupper():
        self.parsing_stack.pop()
        production = self.parsing_table.get_production(parsing_stack_top, self.string[self.string_position])
        self.parsing_stack.push(production)
        print(production)
      else:
        if parsing_stack_top == self.string[self.string_position]:
          self.parsing_stack.pop()
          self.string_position += 1
        else:
          print('Error: Expected', parsing_stack_top, 'but found', self.string[self.string_position])
