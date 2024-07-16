from automatons.automaton import Automaton

class KeywordAutomaton(Automaton):
    def __init__(self):
        super().__init__([
            "DEF",        # def
            "INT",        # int
            "PRINT",      # print
            "RETURN",     # return
            "IF",         # if
            "ELSE"        # else
        ])
    
    def process_char(self, char):
        if self.state == "START":
            if char == 'd':
                self.state = "D"
            elif char == 'i':
                self.state = "I"
            elif char == 'p':
                self.state = "P"
            elif char == 'r':
                self.state = "R"
            elif char == 'e':
                self.state = "E"
            else:
                self.state = "ERROR"

        # Handling 'def'
        elif self.state == "D":
            if char == 'e':
                self.state = "DE"
            else:
                self.state = "ERROR"

        elif self.state == "DE":
            if char == 'f':
                self.state = "DEF"
            else:
                self.state = "ERROR"
            
        elif self.state == "DEF":
            if char:
                self.state = "ERROR"
        
        # Handling 'int'
        elif self.state == "I":
            if char == "n":
                self.state = "IN"
            else:
                self.state = "ERROR"

        elif self.state == "IN":
            if char == "t":
                self.state = "INT"
            else:
                self.state = "ERROR"

        elif self.state == "INT":
            if char:
                self.state = "ERROR"
        
        # Handling 'print'
        elif self.state == "P":
            if char == 'r':
                self.state = "PR"
            else:
                self.state = "ERROR"

        elif self.state == "PR":
            if char == 'i':
                self.state = "PRI"
            else:
                self.state = "ERROR"

        elif self.state == "PRI":
            if char == 'n':
                self.state = "PRIN"
            else:
                self.state = "ERROR"

        elif self.state == "PRIN":
            if char == 't':
                self.state = "PRINT"
            else:
                self.state = "ERROR"

        elif self.state == "PRINT":
            if char:
                self.state = "ERROR"
        
        # Handling 'return'
        elif self.state == "R":
            if char == 'e':
                self.state = "RE"
            else:
                self.state = "ERROR"

        elif self.state == "RE":
            if char == 't':
                self.state = "RET"
            else:
                self.state = "ERROR"

        elif self.state == "RET":
            if char == 'u':
                self.state = "RETU"
            else:
                self.state = "ERROR"

        elif self.state == "RETU":
            if char == 'r':
                self.state = "RETUR"
            else:
                self.state = "ERROR"

        elif self.state == "RETUR":
            if char == 'n':
                self.state = "RETURN"
            else:
                self.state = "ERROR"

        elif self.state == "RETURN":
            if char:
                self.state = "ERROR"
        
        # Handling 'if'
        elif self.state == "I":
            if char == 'f':
                self.state = "IF"
            else:
                self.state = "ERROR"
        
        # Handling 'else'
        elif self.state == "E":
            if char == 'l':
                self.state = "EL"
            else:
                self.state = "ERROR"

        elif self.state == "EL":
            if char == 's':
                self.state = "ELS"
            else:
                self.state = "ERROR"

        elif self.state == "ELS":
            if char == 'e':
                self.state = "ELSE"
            else:
                self.state = "ERROR"

        elif self.state == "ELSE":
            if char:
                self.state = "ERROR"
