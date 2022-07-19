a, b, c = map(int, input().split())
total = a*b
if c < total:
  print(total - c)
else:
  print(0)