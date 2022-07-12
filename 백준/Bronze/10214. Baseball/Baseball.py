T = int(input())
for i in range(T):
  Y = []
  K = []
  for j in range(9):
    y, k = map(int, input().split())
    Y.append(y)
    K.append(k)
  ys = sum(Y)
  kr = sum(K)
  if ys<kr:
    print('Korea')
  elif kr<ys:
    print('Yonsei')
  else:
    print('Draw')