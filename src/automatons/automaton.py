class Automaton:
	def __init__(self, accept_states):
		self.state = "START"
		self.accept_states = set(accept_states)

	def reset(self):
		self.state = "START"

	def is_accepting(self):
		return self.state in self.accept_states 