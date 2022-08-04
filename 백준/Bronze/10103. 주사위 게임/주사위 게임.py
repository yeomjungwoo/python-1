t = int(input())
c = 100
s = 100
for i in range(t):
  a, b = map(int, input().split())
  if b < a:
    s = s - a
  elif a < b:
    c = c - b

print(c)
print(s)