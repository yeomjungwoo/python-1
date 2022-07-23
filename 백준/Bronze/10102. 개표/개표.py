t = int(input())
l = str(input())
s = list(l)
a = s.count('A')
b = s.count('B')
if b < a:
  print('A')
elif a < b:
  print('B')
else:
  print('Tie')