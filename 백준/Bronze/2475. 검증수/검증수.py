a_list = []
a_list = list(map(int, input().split()))
b = []
for i in range(5):
  a = a_list[i]*a_list[i]
  b.append(a)

c = sum(b)
print(c%10)