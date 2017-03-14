import numpy as np
import operator
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
add = 0
for i in numbers:
    add += i
print (add/ N)
if (N % 2 != 0):
    print(numbers[int(N/2)-1])
else:
    print ((numbers[int(N/2)-1] + numbers[int(np.ceil((N+1)/2))-1])/2)
counts = dict()
for i in numbers:
    counts[i] = counts.get(i, 0) + 1
mode = 0
freq = 0
for key in counts.keys():
    if counts[key] >= freq:
        if counts[key] == freq:
            if int(key) < mode :
                mode = key
                freq = counts[key]
        else:
            mode = key
            freq = counts[key]
print(mode)
