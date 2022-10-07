import subprocess
with  open("LeakedPasswordsQ4", "r") as L:
  count = 0
  isDone = False
  for u in L:
   user = u.strip()
   for username in ["charles", "ted", "tom", "bonnie", "clyde", "andrew", "tim"]:
    end_i = user.index(',')
    uname = user[:end_i]
    if username == uname:
      count += 1
      start_i = user.index(',') + 1
      password = user[start_i:].strip()
      string = subprocess.check_output(["python3", "GuardLogin4.pyc", username, password]).decode("utf-8")
      if string.strip() == "Login success!":
        print(user)
        print(string)
        print(count)
        isDone = True
        break
   if isDone: break