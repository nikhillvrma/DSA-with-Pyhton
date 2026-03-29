n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
freq_map = {}
for i in n:
    freq_map[i] = freq_map.get(i, 0)+1
    
for x in m:
    print(f"{x}:{freq_map.get(x, 0)}")