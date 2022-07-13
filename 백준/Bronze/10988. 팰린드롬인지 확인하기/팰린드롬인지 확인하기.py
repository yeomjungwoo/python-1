a = str(input())
a_reverse = ''

for i in a:
  a_reverse = i + a_reverse

if a == a_reverse:
  print(1)
else:
  print(0)