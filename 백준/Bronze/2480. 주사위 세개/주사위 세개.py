d = []
a, b, c = map(int, input().split())
d.append(a)
d.append(b)
d.append(c)
m = max(d)
if a != b and b != c and a != c:
  print(m*100)
elif (a == b and b != c):
  print(1000 + a*100)
elif (b == c and c != a):
  print(1000 + b*100)
elif (c == a and a != b):
  print(1000 + c*100)
else:
  print(10000 + a*1000)