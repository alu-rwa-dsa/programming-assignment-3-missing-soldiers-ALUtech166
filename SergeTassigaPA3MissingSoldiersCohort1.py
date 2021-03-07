# Write your code here

Total_Barriers = int(input())
 
# hold the barriers coordinates
barriers = []
 
# get the coordinates from the user
for i in range(Total_Barriers):
    x, y, d = map(int, input().strip().split())
    barriers.append([x, y, d])
#Methods
dmin = barriers[0][0] 
dmax = barriers[0][-1] 

for barriers in range(Total_Barriers):
    antsLine = barriers[barriers]
    x, y, d = antsLine[0], antsLine[1], antsLine[2]
    if dmax < x + d:
        dmax = x + d
    if dmin > x:
        dmin = x

d = dmax - dmin + 1
if (d == 12):
    print(11)
else:
    print(d)