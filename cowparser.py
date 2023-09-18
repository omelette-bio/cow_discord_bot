#!/usr/bin/env python3

import os, argparse, sys, time

def move_cursor(n):
  global cursor
  cursor += n
  if cursor < 0 or cursor > 29999:
    print("Error: cursor out of bounds")
    sys.exit(1)

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
  global data, cursor
  if target_type == "ascii":
    print(chr(data[cursor]), end = '')
  elif target_type == "int":
    print(data[cursor])

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
  global exec_map, COW_KEYWORDS
  try:
    func = COW_KEYWORDS[block]
  except:
    print("Error: invalid block")
    sys.exit(1)
  func = exec_map[func]
  if func == None:
    print("Error: 3 is an invalid data : it would cause an infinite loop")
    sys.exit(1)
  else:
    exec(func)

def MOO():
  global data, cursor, i, words
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
      print("Error: no matching moo")
      sys.exit(1)
    else:
      i = moo_pos
  
def moo():
  global data, cursor, i, words
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
      print("Error: no matching MOO")
      sys.exit(1)
    else:
      i = MOO_pos

parser = argparse.ArgumentParser(description='Cow Interpreter')
parser.add_argument('file', help = 'cow file to interpret')

args = parser.parse_args()

if not os.path.isfile(args.file):
  print("Error: file does not exist")
  sys.exit(1)

if args.file[-4:] != ".cow":
  print("Error: file is not a cow file")
  sys.exit(1)

f = os.open(args.file, os.O_RDONLY)
code = os.read(f, os.path.getsize(args.file))

COW_KEYWORDS=("moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom")
exec_map = {"moo": "moo()", "mOo": "move_cursor(-1)", "moO": "move_cursor(1)", "mOO": None, "Moo": "Moo()", "MOo": "set_block(data[cursor] - 1)", "MoO": "set_block(data[cursor] + 1)", "MOO": "MOO()", "OOO": "set_block(0)", "MMM": "register_operation()", "OOM": "display_block('int')", "oom": "input_block()"}

# transform code into a list
code = code.decode('utf-8').split('\n')

# get a list of all words and exclude words that are not cow keywords
words = []
for line in code:
  for word in line.split():
    if word in COW_KEYWORDS:
      words.append(word)

data = [0] * 30000
cursor = 0
register = None
i = 0
end = len(words)
  

while i < end:
  #print(f"{words[i]}: {data[:3]}: {cursor}: {i}")
  match words[i]:
    case "mOo":
      move_cursor(-1)
    
    case "moO":
      move_cursor(1)
    
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
      execute_block(data[cursor])
    
    case "MOO":
      MOO()
    
    case "moo":
      moo()
  
  
  i += 1