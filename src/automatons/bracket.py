from automatons.automaton import Automaton

class BracketAutomaton(Automaton):
	def __init__(self):
		super().__init__(["BRACKET"])
  
	def process_char(self, char):
		if self.state == "START":
			if char == "{" or char == "}" or char == "(" or char == ")" or char == "[" or char == "]":
				self.state = "BRACKET"
			else:
				self.state = "NOT_A_BRACKET"
		
		elif self.state == "BRACKET":
			if (char):
				self.state = "NOT_A_BRACKET"
  
