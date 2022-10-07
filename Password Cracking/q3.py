import subprocess
with  open("dictionary", "r") as d:
  count = 0
  isDone = False
  for word in d:
   for char in ["!","@","#"]:
    password = word.strip()
    for i in range(len(password)+1):
      p = password[:i] + char + password[i:]
      count += 1
      string = subprocess.check_output(["python3", "GuardLogin3.pyc", "Al", p]).decode("utf-8")
      if count % 5000 == 0:
        print(p)
        print(string)
      if string.strip() == "Login success!":
        isDone = True
        print(p)
        print(string)
        print(count)
        break
      count += 1
      string = subprocess.check_output(["python3", "GuardLogin3.pyc", "AL", p]).decode("utf-8")
      if count % 5000 == 0:
        print(p)
        print(string)
      if string.strip() == "Login success!":
        isDone = True
        print(p)
        print(string)
        print(count)
        break
    if isDone: break
   if isDone: break
