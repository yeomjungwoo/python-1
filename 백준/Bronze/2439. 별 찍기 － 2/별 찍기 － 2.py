a = int(input())
for i in range(a):
  b = '*'*(i+1)
  c = b.rjust(a)
  print(c)