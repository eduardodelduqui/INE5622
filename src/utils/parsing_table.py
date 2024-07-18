class ParsingTable:
  def __init__(self):
    self.productions = {
        'A': {'a': ['C'], 'b': ['B'], 'c': ['B'], 'e': ['B'], 'g': ['b'], 'i': ['B'], 'j': ['B'], 'k': ['B'], '$': ['λ']},
        'B': {'b': ['Jg'], 'c': ['cbg'], 'e': ['eHf'], 'g': ['g'], 'i': ['Lg'], 'j': ['Mg'], 'k': ['N'], '$': ['λ']},
        'C': {'a': ['ED'] },
        'D': {'a': ['ED'], '$': ['λ']},
        'E': {'a': ['abtFueHf'] },
        'F': {'c': ['cbG'] },
        'G': {'d': ['dcbG'], 'u': ['λ']},
        'H': {'b': ['BI'], 'c': ['BI'], 'e': ['BI'], 'g': ['BI'], 'i': ['BI'], 'j': ['BI'], 'k': ['BI']},
        'I': {'b': ['BI'], 'c': ['BI'], 'e': ['BI'], 'f': ['λ'], 'g': ['BI'], 'i': ['BI'], 'j': ['BI'], 'k': ['BI']},
        'J': {'b': ['bhK'] },
        'K': {'b': ['PR'], 's': ['P'], 't': ['P']},
        'L': {'i': ['iP'] },
        'M': {'j': ['j'] },
        'N': {'k': ['ktPuBO'] },
        'O': {'b': ['λ'], 'c': ['λ'], 'e': ['λ'], 'f': ['λ'], 'g': ['λ'], 'i': ['λ'], 'j': ['λ'], 'k': ['λ'], 'l': ['λIB'], '$': ['λ']},
        'P': {'b': ['VQ'], 's': ['VQ'], 't': ['VQ']},
        'Q': {'g': ['λ'], 'm': ['mV'], 'n': ['nv'], 'o': ['ov'], 'u': ['λ']},
        'R': {'b': ['btSu'] },
        'S': {'b': ['bT']},
        'T': {'d': ['dbT'], 'u': ['λ']},
    }
    ##.... Continuar copiando tabela do jflap								

  def get_production(self, non_terminal, terminal):
    return self.productions[non_terminal][terminal]
