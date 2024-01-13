#BAEKJOON 10820
while True :
  lower = 0
  upper = 0
  number = 0
  blank = 0

  try :
    s = input()
    for i in range(len(s)) :
      if 97 <= ord(s[i]) <= 122 :
        lower += 1
      elif 65 <= ord(s[i]) <= 90 :
        upper += 1
      elif s[i] == ' ' :
        blank += 1
      else :
        number += 1
  except :
    break
  
  print(lower, upper, number, blank)
  