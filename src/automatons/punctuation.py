from automatons.automaton import Automaton

class PunctuationAutomaton(Automaton):
    def __init__(self):
        super().__init__([
            "COMMA",        # ,
            "COLON",        # :
            "SEMICOLON"
        ])
    
    def process_char(self, char):
        if self.state == "START":
            if char == ':':
                self.state = "COLON"
            elif char == ',':
                self.state = "COMMA"
            elif char == ';':
                self.state = "SEMICOLON"
            else:
                self.state = "ERROR"
        
        elif self.state == "COLON":
            if char:
                self.state = "ERROR"

        elif self.state == "COMMA":
            if char:
                self.state = "ERROR"

        elif self.state == "SEMICOLON":
            if char:
                self.state = "ERROR"
