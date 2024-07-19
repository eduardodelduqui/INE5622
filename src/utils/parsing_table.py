class ParsingTable:
  def __init__(self):
    #No K tanto P quanto R produz b
    #No O tanto lB quanto λ produz l
    self.productions = {
        'A': {'a': 'C', 'b': 'B', 'c': 'B', 'e': 'B', 'g': 'B', 'i': 'B', 'j': 'B', 'k': 'B', '$': 'λ'},
        'B': {'b': 'Jg', 'c': 'cbg', 'e': 'eHf', 'g': 'g', 'i': 'Lg', 'j': 'Mg', 'k': 'N'},
        'C': {'a': 'ED'},
        'D': {'a': 'C', '$': 'λ'},
        'E': {'a': 'abtFueHf'},
        'F': {'c': 'cbG', 'u': 'λ' },
        'G': {'d': 'dF', 'u': 'λ'},
        'H': {'b': 'BI', 'c': 'BI', 'e': 'BI', 'g': 'BI', 'i': 'BI', 'j': 'BI', 'k': 'BI'},
        'I': {'b': 'H', 'c': 'H', 'e': 'H', 'f': 'λ', 'g': 'H', 'i': 'H', 'j': 'H', 'k': 'H'},
        'J': {'b': 'bhK' },
        'K': {'b': 'R', 's': 'P', 't': 'P'},
        'L': {'i': 'iP' },
        'M': {'j': 'j' },
        'N': {'k': 'ktPuBO' },
        'O': {'b': 'λ', 'c': 'λ', 'e': 'λ', 'f': 'λ', 'g': 'λ', 'i': 'λ', 'j': 'λ', 'k': 'λ', 'l': 'lB', '$': 'λ'},
        'P': {'b': 'VQ', 's': 'VQ', 't': 'VQ'},
        'Q': {'g': 'λ', 'm': 'mV', 'n': 'nv', 'o': 'ov', 'u': 'λ'},
        'R': {'b': 'btSu' },
        'S': {'b': 'bT', 'u': 'λ'},
        'T': {'d': 'dS', 'u': 'λ'},
        'V': {'b': 'WX', 's': 'WX', 't': 'WX'},
        'W': {'b': 'ZY', 's': 'ZY', 't': 'ZY'},
        'X': {'g': 'λ', 'm': 'λ', 'n': 'λ', 'o': 'λ', 'p': 'pWX', 'q': 'qXW', 'u': 'λ'},
        'Y': {'g': 'λ', 'm': 'λ', 'n': 'λ', 'o': 'λ', 'p': 'λ', 'q': 'λ', 'r': 'rZY', 'u': 'λ'},
        'Y': {'b': 'b', 's': 's', 't': 'tVu'}
    }	
    # self.productions = {
    #     'A': {'a': ['C'], 'b': ['B'], 'c': ['B'], 'e': ['B'], 'g': ['B'], 'i': ['B'], 'j': ['B'], 'k': ['B'], '$': ['λ']},
    #     'B': {'b': ['Jg'], 'c': ['cbg'], 'e': 'eHf', 'g': 'g', 'i': 'Lg', 'j': 'Mg', 'k': 'N'},
    #     'C': {'a': 'ED'},
    #     'D': {'a': 'C', '$': 'λ'},
    #     'E': {'a': 'abtFueHf'},
    #     'F': {'c': 'cbG', 'u': 'λ' },
    #     'G': {'d': 'dF', 'u': 'λ'},
    #     'H': {'b': 'BI', 'c': 'BI', 'e': 'BI', 'g': 'BI', 'i': 'BI', 'j': 'BI', 'k': 'BI'},
    #     'I': {'b': 'H', 'c': 'H', 'e': 'H', 'f': 'λ', 'g': 'H', 'i': 'H', 'j': 'H', 'k': 'H'},
    #     'J': {'b': 'bhK' },
    #     'K': {'b': 'R', 's': 'P', 't': 'P'},
    #     'L': {'i': 'iP' },
    #     'M': {'j': 'j' },
    #     'N': {'k': 'ktPuBO' },
    #     'O': {'b': 'λ', 'c': 'λ', 'e': 'λ', 'f': 'λ', 'g': 'λ', 'i': 'λ', 'j': 'λ', 'k': 'λ', 'l': 'lB', '$': 'λ'},
    #     'P': {'b': 'VQ', 's': 'VQ', 't': 'VQ'},
    #     'Q': {'g': 'λ', 'm': 'mV', 'n': 'nv', 'o': 'ov', 'u': 'λ'},
    #     'R': {'b': 'btSu' },
    #     'S': {'b': 'bT', 'u': 'λ'},
    #     'T': {'d': 'dS', 'u': 'λ'},
    #     'V': {'b': 'WX', 's': 'WX', 't': 'WX'},
    #     'W': {'b': 'ZY', 's': 'ZY', 't': 'ZY'},
    #     'X': {'g': 'λ', 'm': 'λ', 'n': 'λ', 'o': 'λ', 'p': 'pWX', 'q': 'qXW', 'u': 'λ'},
    #     'Y': {'g': 'λ', 'm': 'λ', 'n': 'λ', 'o': 'λ', 'p': 'λ', 'q': 'λ', 'r': 'rZY', 'u': 'λ'},
    #     'Y': {'b': 'b', 's': 's', 't': 'tVu'}
    # }								

  def get_production(self, terminal, non_terminal):
    return self.productions[terminal][non_terminal]
