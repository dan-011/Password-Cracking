import random
import hashlib
import os
import binascii

salts = set()
_salts = set()
with open("LeakedPasswordsQ6", "r") as L:
  for user in L:
    first_b = user.index("b'")
    u = user[first_b+5:]
    start_i = u.index("b'")
    salt = u[start_i:].strip()
    _salts.add(salt)
  for salt in _salts:
    if ',' in salt:
      i = salt.index(',')+1
      new = salt[i:]
      salts.add(new)
    else:
      salts.add(salt)
hashed_dict = {}
salt_strings = []
with open("dictionary", "r") as d:
  for w in d:
    for s in salts:
      salt = s[2:-1]
      hash1 = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(w.strip(),'utf-8'), bytes.fromhex(salt), 100))
      hashed_dict[str(hash1)] = w.strip()
guards = []
with open("LeakedPasswordsQ6", "r") as L:
  for user in L:
    start_i = user.index("b'")
    u = user[start_i:]
    end_i = u.index(',')
    hashed_pass = u[:end_i].strip()
    #print(hashed_pass)
    nums = hashed_pass[2:-1]
    username = user[:start_i].strip()
    if hashed_pass in hashed_dict:
      guards.append((username, hashed_dict[hashed_pass]))
for guard in guards:
  print(guard[0] + " " + guard[1])