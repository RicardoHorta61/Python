# iven a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return (print(str))
  else:
    return print("not "+ str)

not_string('candy') #→ 'not candy'
not_string('x') #→ 'not x'
not_string('not bad') #→ 'not bad'