from automatons.automaton import Automaton

class ArithmeticOperatorAutomaton(Automaton):
    def __init__(self):
        super().__init__([
            "PLUS",             # +
            "MINUS",            # -
            "MULTIPLY",         # *
        ])
    
    def process_char(self, char):
        if self.state == "START":
            if char == '+':
                self.state = "PLUS"
            elif char == '-':
                self.state = "MINUS"
            elif char == '*':
                self.state = "MULTIPLY"
            else:
                self.state = "ERROR"

