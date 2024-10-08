from automatons.automaton import Automaton

class NumberAutomaton(Automaton):
	def __init__(self):
		super().__init__(["INTEGER"])
  
	def process_char(self, char):
		if self.state == "START":
			if char.isdigit():
				self.state = "INTEGER"
			else:
				self.state = "NOT_A_NUMBER"
		
		elif self.state == "INTEGER":
			if char.isdigit():
				self.state = "INTEGER"
			else:
				self.state = "NOT_A_NUMBER"
