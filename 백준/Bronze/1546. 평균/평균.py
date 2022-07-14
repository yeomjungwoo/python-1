sub = int(input())
num_list = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 
m = max(num_list)
for i in range(sub):
  num_list[i] = num_list[i]/m*100
s = sum(num_list)

print(s/sub)