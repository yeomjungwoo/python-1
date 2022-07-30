t = int(input())
s = list(map(int, input().split()))
d = 0

for i in range(t):

  num = s[i]
  a = 0

  
  for i in range(1, num+1):
    if num % i == 0:
        # 약수임
        a += i  
  if a == num+1:
    d += 1
print(d)