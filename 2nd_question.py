# x = int(input())
# sames = []
# diff = []
placement = []

# for i in range(x): # Must be in the group
#     must = input()
#     sames.append(must)
# print(sames)

# different = int(input())

# for g in range(different): # have to be in different groups
#     not_together = input()
#     diff.append(not_together)
# print(diff)

place = int(input()) # there actual groups so compare 
for i in range(place):
    groups = input()
    placement.append(groups)
print(placement)

# compare all groups to the musts and differents

for i in groups:  # different comparison to pre-existing group
    print(i)
        
        

 
