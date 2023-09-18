def move_cursor(n):
  global cursor, output
  cursor += n
  if cursor < 0 or cursor > 29999:
    output = "Error: cursor out of bounds"
    return False
  return True

def set_block(n):
  global cursor, data
  data[cursor] = n

def register_operation():
  global data, cursor, register
  if register == None:
    register = data[cursor]
  else:
    data[cursor] = register
    register = None

def display_block(target_type):
  global data, cursor, output
  if target_type == "ascii":
    output += chr(data[cursor])
  elif target_type == "int":
    output += str(data[cursor])+'\n'

def input_block():
  global data, cursor
  data[cursor] = int(input("Input: "))

def Moo():
  global data, cursor
  if data[cursor] == 0:
    char = input("Input: ")
    data[cursor] = ord(char)
  else:
    display_block("ascii")

def execute_block(block):
  global exec_map, COW_KEYWORDS, output
  try:
    func = COW_KEYWORDS[block]
  except:
    output = "Error: invalid block"
    return False
  func = exec_map[func]
  if func == None:
    output = "Error: 3 is an invalid block, would cause infinite loop"
    return False
  else:
    exec(func)
    return True

def MOO():
  global data, cursor, i, words, output
  if data[cursor] == 0:
    tmp = i+1
    MOO_cpt = 0
    moo_pos = -1
    while tmp < len(words):
      if words[tmp] == "MOO":
        MOO_cpt += 1
      elif words[tmp] == "moo":
        if MOO_cpt == 0:
          moo_pos = tmp
          break
        else:
          MOO_cpt -= 1
      tmp += 1
    if moo_pos == -1:
      output = "Error: no matching moo"
      return False
    else:
      i = moo_pos
      return True
  
def moo():
  global data, cursor, i, words, output
  if data[cursor] != 0:
    tmp = i-1
    moo_cpt = 0
    MOO_pos = -1
    while tmp >= 0:
      if words[tmp] == "moo":
        moo_cpt += 1
      elif words[tmp] == "MOO":
        if moo_cpt == 0:
          MOO_pos = tmp
          break
        else:
          moo_cpt -= 1
      tmp -= 1
    if MOO_pos == -1:
      output = "Error: no matching MOO"
      return False
    else:
      i = MOO_pos
      return True

def init(input):
  global code, COW_KEYWORDS
  code = input.split()
  words = []
  for line in code:
    for word in line.split():
      if word in COW_KEYWORDS:
        words.append(word)
  return words


COW_KEYWORDS=("moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom")
exec_map = {"moo": "moo()", "mOo": "move_cursor(-1)", "moO": "move_cursor(1)", "mOO": None, "Moo": "Moo()", "MOo": "set_block(data[cursor] - 1)", "MoO": "set_block(data[cursor] + 1)", "MOO": "MOO()", "OOO": "set_block(0)", "MMM": "register_operation()", "OOM": "display_block('int')", "oom": "input_block()"}


def main(words):
  global data, cursor, register, i, output
  data = [0] * 30000
  cursor = 0
  register = None
  i = 0
  end = len(words)
  output = ""

  while i < end:
    #print(f"{words[i]}: {data[:3]}: {cursor}: {i}")
    match words[i]:
      case "mOo":
        result = move_cursor(-1)
        if result == False:
          return output
      
      case "moO":
        result = move_cursor(1)
        if result == False:
          return output
      
      case "MOo":
        set_block(data[cursor] - 1)
      
      case "MoO":
        set_block(data[cursor] + 1)
      
      case "OOO":
        set_block(0)
      
      case "MMM":
        register_operation()
      
      case "OOM":
        display_block("int")
      
      case "Moo":
        Moo()
      
      case "oom":
        input_block()
      
      case "mOO":
        result = execute_block(data[cursor])
        if result == False:
          return output
        
      case "MOO":
        result = MOO()
        if result == False:
          return output
      
      case "moo":
        result = moo()
        if result == False:
          return output
    
    i += 1
  return output