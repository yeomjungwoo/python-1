while True:
  a = str(input()) 
  s = list(a) 
  int_list = list(map(int, s))
  c = list(reversed(int_list))
  if int_list[0] == 0 and len(int_list) == 1:
    break
  elif int_list == c:
    print('Yes')

  else:
    print('No')
