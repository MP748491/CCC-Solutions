
iterations = int(input())
replay = str(iterations)
first = 100
second = 100

for i in range(iterations):
    rolls = input()
    compare = (list(map(int, rolls.split())))
    if compare[0] > compare[1]:
        second = second - compare[0]
    elif compare[1] > compare[0]:
        first = first - compare[1]
    elif compare[1] == compare[0]:
        second = second
        first = first 


print(first)
print(second)



