import random
import hashlib
import os
import binascii

hashed_dictionary = {}
with open("dictionary", "r") as d:
  for i in d:
      m = hashlib.sha256()
      m.update(bytes(i.strip(), 'utf-8'))
      hash1 = m.hexdigest()
      hashed_dictionary[hash1] = i.strip()
dumb_guards = []
with open("LeakedPasswordsQ5", "r") as L:
  for user in L:
    start_i = user.index(',')
    username = user[:start_i].strip()
    _hash = user[start_i+1:].strip()
    if _hash in hashed_dictionary:
      dumb_guards.append((username, hashed_dictionary[_hash]))
f = open("dumb_guards.txt", "w+")
for guard in dumb_guards:
  f.write(guard[0] + ", " + guard[1] +"\n")
f.close()