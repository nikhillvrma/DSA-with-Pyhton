"""
Constraints
1. 1 < n[i] < 10
2. n can have 10^8 elements
3. m can have 10^8 elements
"""

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_list = [0]*11
for nums in n:
    hash_list[nums] += 1
    
for x in m:
    if x < 1 or x > 10:
        print(0)
    else:
        print(f"{x}:{hash_list[x]}")