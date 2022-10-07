with open("dictionary", "r") as d:
  sum = 0
  counter = 0
  for w in d:
    word = w.strip()
    sum += len(word)
    counter += 1
  print("Average Word Length: " + str(sum/counter))
  print("Number of Words " + str(counter))