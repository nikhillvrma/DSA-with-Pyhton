word = "my name is nikhil verma"
c = ['n', 'a', 'm', 's', 'z']
frequency = {}

for i in word:
    frequency[i] = frequency.get(i, 0)+1

for j in c:
    print(f"{j}:{frequency.get(j, 0)}")