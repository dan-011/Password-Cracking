import subprocess
with  open("dictionary", "r") as d:
  counter = 0
  for word in d:
    counter += 1
    string = subprocess.check_output(["python3", "GuardLogin2.pyc", "Al", word.strip()])
    string = string.decode("utf-8")
    if string.strip() == "Login success!":
      print(word)
      print(counter)
      break
    string = subprocess.check_output(["python3", "GuardLogin2.pyc", "AL", word.strip()])
    string = string.decode("utf-8")
    counter += 1
    if string.strip() == "Login success!":
      print(word)
      print(counter)
      break
    