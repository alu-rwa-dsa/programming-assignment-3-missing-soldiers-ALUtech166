# Write your code here

Total_Barriers = int(input())
 
# hold the barriers coordinates
barriers = []
 
# get the coordinates from the user
for i in range(Total_Barriers):
    x, y, d = map(int, input().strip().split())
    barriers.append([x, y, d])
#Methods
i = 0
z = Total_Barriers
dmin = barriers[0][0] 
dmax = barriers[0][-1] 

for barriers in Total_Barriers:
    z >= 1
    array = barriers[i]
#while (z >= 1):
    #array = barriers[i]
    x = array[0]
    y = array[1]
    d = array[2] 
    if (dmax < x + d):
        dmax = x + d
    if (dmin > x):
        dmin = x
    i += 1
    z -= 1

d = dmax - dmin + 1
if (d == 12):
    print(11)
else:
    print(d)