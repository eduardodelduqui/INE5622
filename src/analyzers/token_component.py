class Token:
  def __init__(self, type, value, line, column):
    self.type = type
    self.value = value
    self.line = line
    self.column = column

  def __repr__(self):
    if self.type == "id":
      return "id"
    elif self.type == "num":
      return "num"
    else:
      return self.value