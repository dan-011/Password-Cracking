import sys
import random
import hashlib
import os
import binascii
import math
from math import floor

count = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols=['&', '=', '!', '?', '.', '~', '*', '^', '#', '$']
with open("dictionary", "r") as d:
  with open("hash_to_crack2", "r") as htc2:
    for h in htc2:
      for w in d:
        word = w.strip()
        for i in range(10):
          for j in range(len(word)):
            num_w = word[:j] + numbers[i] + word[j:]
            for k in range(10):
              for r in range(len(num_w)):
                count += 1
                ns_w = num_w[:r] + symbols[k] + num_w[r:]
                m = hashlib.sha256()
                m.update(bytes(ns_w, 'utf-8'))
                _hash = m.hexdigest()
                if _hash == h.strip():
                  print(ns_w)
                  print("Guesses: " + str(count))
                  exit(0)
