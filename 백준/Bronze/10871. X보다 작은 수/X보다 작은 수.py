a, b = map(int, input().split())
c = map(int, input().split())
s = list(c)
d = []
for i in range(a):
  if s[i] < b:
    d.append(s[i])
print(*d)