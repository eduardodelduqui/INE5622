from automatons.automaton import Automaton

class IdentifierAutomaton(Automaton):
    def __init__(self):
        super().__init__(["IDENTIFIER"])
    
    def process_char(self, char):
        if self.state == "START":
            if char.isalpha() or char == '_':
                self.state = "IDENTIFIER"
            else:
                self.state = "ERROR"
        
        elif self.state == "IDENTIFIER":
            if char.isalnum() or char == '_':
                self.state = "IDENTIFIER"
            else:
                self.state = "ERROR"
