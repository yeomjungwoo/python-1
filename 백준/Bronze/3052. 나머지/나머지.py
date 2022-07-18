a = []
for i in range(10):
  b = int(input())
  c = b%42
  a.append(c)

a_set = set(a)
a_list = list(a_set)
d = len(a_list)
print(d)