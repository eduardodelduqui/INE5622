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
    while not self.parsing_stack.is_empty():
      parsing_stack_top = self.parsing_stack.get_top()
      # print(parsing_stack_top)
      if parsing_stack_top.isupper():
        self.parsing_stack.pop()
        try:
          production = self.parsing_table.get_production(parsing_stack_top, self.string, self.string_position)
        except KeyError as error:
          print("Erro!")
          print(f'Entrada vazia: Token "{self.string[self.string_position]}" Simbolo nao terminal "{parsing_stack_top}"')
          break
        else:
          self.parsing_stack.push(production)
        
      else:
        if parsing_stack_top == self.string[self.string_position]:
          self.parsing_stack.pop()
          self.string_position += 1
        elif parsing_stack_top == 'λ':
          self.parsing_stack.pop()
        else:
          print('Erro: Esperado', self.string[self.string_position], 'encontrado', parsing_stack_top)
          break
    if self.parsing_stack.is_empty():
      print("Sucesso!")
