#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) <= 1:
    return print(str)
  else:
    meio = str[1:len(str)-1]
    return print(str[len(str)-1] + meio + str[0])

front_back("OLA")
front_back("4_3_2_1")
front_back("a")