import subprocess
with  open("MostCommonPWs", "r") as pwds:
  counter = 0
  for word in pwds:
    counter += 1
    string = subprocess.check_output(["python3", "GuardLogin1.pyc", "adam", word.strip()]).decode("utf-8")
    if string.strip() == "Login success!":
      print(word)
      print(counter)
      break