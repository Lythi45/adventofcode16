from itertools import permutations
tris=map(lambda s:map(int,s.split()),open("input03.txt",'r').readlines())
su=0
for tri0 in tris:
    tri1=next(tris)
    tri2=next(tris)
    for i in range(3):
        tr=True
        for sides in permutations([next(tri0),next(tri1),next(tri2)]):
            if sides[0]+sides[1]<=sides[2]:
                tr=False
        if tr:
            su+=1
print(su)
