from automatons.number import NumberAutomaton
from automatons.relop import RelationalOperatorAutomaton
from automatons.bracket import BracketAutomaton
from automatons.arithmetic import ArithmeticOperatorAutomaton
from automatons.keyword import KeywordAutomaton
from automatons.identifier import IdentifierAutomaton
from automatons.punctuation import PunctuationAutomaton
from automatons.assign import AssignAutomaton
from token_component import Token

class LexerError(Exception):
    pass

class AnalisadorLexico:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.length = len(input)
        self.buffer = {
            "type": '',
            "value": ''
        }
        self.maxString = ''
        self.tokens = []
        self.number_automaton = NumberAutomaton()
        self.relop_automaton = RelationalOperatorAutomaton()
        self.bracket_automaton = BracketAutomaton()
        self.arithmetic_automaton = ArithmeticOperatorAutomaton()
        self.keyword_automaton = KeywordAutomaton()
        self.identifier_automaton = IdentifierAutomaton()
        self.punctuation_automaton = PunctuationAutomaton()
        self.assign_automaton = AssignAutomaton()

    def reset_automatons(self):
        self.number_automaton.reset()
        self.relop_automaton.reset()
        self.bracket_automaton.reset()
        self.arithmetic_automaton.reset()
        self.keyword_automaton.reset()
        self.identifier_automaton.reset()
        self.punctuation_automaton.reset()
        self.assign_automaton.reset()

    def clear_buffer(self):
        self.buffer = {
            "type": '',
            "value": ''
        }

    def get_token_values(self):
        return [token.value for token in self.tokens]
        
    def get_tokens(self):
        lines = self.input.split('\n')
        
        for line_number, line in enumerate(lines, start=1):
            column_number = 1
            word_position = 0
            while word_position < len(line):
                char = line[word_position].strip()

                if not bool(char):
                    if self.buffer["value"]:
                        token = Token(self.buffer["type"], self.buffer["value"], line_number, column_number - len(self.buffer["value"]))
                        self.tokens.append(token)
                        self.reset_automatons()
                        self.clear_buffer()
                        continue
                    else:
                        self.reset_automatons()
                        self.clear_buffer()
                        column_number += 1
                        word_position += 1
                        continue

                tryToken = self.tryToken(char)

                # Se buffer tem valor e o tryToken é falso, tokeniza e reseta os autômatos
                if self.buffer["value"] and not tryToken:
                    token = Token(self.buffer["type"], self.buffer["value"], line_number, column_number - len(self.buffer["value"]))
                    self.tokens.append(token)
                    self.reset_automatons()
                    self.clear_buffer()
                    continue  # Volta para reavaliar o mesmo caractere atual

                # Adiciona o caractere atual ao buffer se tryToken é verdadeiro
                if tryToken:
                    self.buffer["value"] += char
                    self.buffer["type"] = tryToken
                    column_number += 1
                    word_position += 1
                else:
                    raise LexerError(f"Caractere inesperado '{char}' na linha {line_number}, coluna {column_number}")

                # Se buffer tem valor e estamos no fim da linha, tokeniza e reseta os autômatos
                if self.buffer["value"] and word_position == len(line):
                    token = Token(self.buffer["type"], self.buffer["value"], line_number, column_number - len(self.buffer["value"]))
                    self.tokens.append(token)
                    self.reset_automatons()
                    self.clear_buffer()
                    column_number += 1
                    word_position += 1

        return self.tokens

    def tryToken(self, char):
        self.number_automaton.process_char(char)
        self.relop_automaton.process_char(char)
        self.bracket_automaton.process_char(char)
        self.arithmetic_automaton.process_char(char)
        self.keyword_automaton.process_char(char)
        self.identifier_automaton.process_char(char)
        self.punctuation_automaton.process_char(char)
        self.assign_automaton.process_char(char)

        if self.assign_automaton.is_accepting():
            return "assign"
        if self.punctuation_automaton.is_accepting():
            return "punctuation"
        if self.number_automaton.is_accepting():
            return "num"
        if self.relop_automaton.is_accepting():
            return "relop"
        if self.bracket_automaton.is_accepting():
            return "bracket"
        if self.arithmetic_automaton.is_accepting():
            return "arithmetic"
        if self.keyword_automaton.is_accepting():
            return "keyword"
        if self.identifier_automaton.is_accepting() and not self.keyword_automaton.is_accepting():
            return "id"

input = """
def func1 ( int5 A , int B )
{
    int C = A + B ;
    int D = B * C ;
    return ;
}
def principal ()
{
    int C ;
    int D ;
    int R ;
    C = 4 ;
    D = 5.0 ;
    R = func1 ( C , D ) ;
    return ;
}
"""

lexer = AnalisadorLexico(input)
tokens = lexer.get_tokens()
token_values = lexer.get_token_values() #### Usar esse token_values caso queira pegar os valores
print(tokens)
