T = int(input())
for i in range(T):
  name = ''
  max = 0
  t = int(input())
  for j in range(t):
    x, y = input().split()
    y = int(y)
    if max < y:
      name = x
      max = y

  print(name)