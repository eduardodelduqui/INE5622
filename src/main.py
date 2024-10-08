from analyzers.lexical import LexicalAnalyzer
from analyzers.syntax import SyntaxAnalyzer
from os import path

caminho = path.dirname(__file__) + "/tests/test1.lsi"
with open(caminho, 'r') as arquivo:
    input = arquivo.read()

terminal_to_symbol = {"def": "a", 
                      "id": "b", 
                      "int": "c", 
                      ",": "d", 
                      "{": "e",
                      "}": "f",
                      ";": "g", 
                      "=": "h", 
                      "print": "i", 
                      "return": "j", 
                      "if": "k", 
                      "else": "l", 
                      "<": "m", 
                      ">":"n", 
                      "==": "o",
                      "+": "p",
                      "-": "q", 
                      "*": "r",
                      "num": "s",
                      "(": "t",
                      ")": "u"}

lexer = LexicalAnalyzer(input)
tokens = lexer.get_tokens()
print(tokens)
print("---------------------------")
tokens = list(map(lambda t : t.toString(), tokens))
symbols = list(map(lambda t : terminal_to_symbol[t], tokens))
syntax_input = ''.join(symbols)
syntax = SyntaxAnalyzer()
syntax.process(syntax_input)
