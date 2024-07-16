from automatons.automaton import Automaton

class AssignAutomaton(Automaton):
    def __init__(self):
        super().__init__([
            "ASSIGN",        # =
        ])
    
    def process_char(self, char):
        if self.state == "START":
            if char == '=':
                self.state = "ASSIGN"
        
        elif self.state == "ASSIGN":
            if char:
                self.state = "ERROR"
