from itertools import permutations
tris=map(lambda s:map(int,s.split()),open("input03.txt",'r').readlines())
su=0
for tri in tris:
    tr=True
    for sides in permutations(tri):
        if sides[0]+sides[1]<=sides[2]:
            tr=False
    if tr:
        su+=1
print(su)
