
from collections import Counter

year = input()

year_int = (list(map(int, year)))

for i in year_int: #-> [2, 0, 1, 3] 
    if i == i[+1]:
        print('dup')




