from analyzers.lexical import LexicalAnalyzer
from os import path

caminho = path.dirname(__file__) + "/tests/test1.lsi"
with open(caminho, 'r') as arquivo:
    input = arquivo.read()

lexer = LexicalAnalyzer(input)
tokens = lexer.get_tokens()
token_values = lexer.get_token_values() #### Usar esse token_values caso queira pegar os valores
print(tokens)
