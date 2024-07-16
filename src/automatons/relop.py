from automatons.automaton import Automaton

class RelationalOperatorAutomaton(Automaton):
    def __init__(self):
        super().__init__([
                "EQUAL_EQUAL",      # ==
                "GREATER",          #>
                "LESS",             #<
            ])
		
    def process_char(self, char):
        if self.state == "START":
            if char == '=':
                self.state = "EQUAL"
            elif char == '>':
                self.state = "GREATER"
            elif char == '<':
                self.state = "LESS"
            else:
                self.state = "ERROR"

            
        elif self.state == "EQUAL":
            if char == '=':
                self.state = "EQUAL_EQUAL"
            else:
                self.state = "ERROR"

