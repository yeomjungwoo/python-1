num_list = []
for i in range(9):
  a = int(input())
  num_list.append(a)
m = max(num_list)
index = num_list.index(m) #최댓값의 인덱스 찾기
print(m)
print(index + 1)