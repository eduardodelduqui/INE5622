from automatons.automaton import Automaton

class NumberAutomaton(Automaton):
	def __init__(self):
		super().__init__(["INTEGER", "FLOAT"])
  
	def process_char(self, char):
		if self.state == "START":
			if char.isdigit():
				self.state = "INTEGER"
			else:
				self.state = "NOT_A_NUMBER"
		
		elif self.state == "INTEGER":
			if char.isdigit():
				self.state = "INTEGER"
			if char == ".":
				self.state = "POINT"
			else:
				self.state = "NOT_A_NUMBER"

		elif self.state == "POINT":
			if char.isdigit():
				self.state = "FLOAT"
			else:
				self.state = "ERROR"  
