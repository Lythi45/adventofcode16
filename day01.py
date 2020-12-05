walks=map(lambda s:s.strip(),open("input01.txt",'r').readline().split(','))
pset=set()
first=False
px=0
py=0
dir=0
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
for walk in walks:
    if walk[0]=='R':
        dir=(dir+1)%4
    else:
        dir=(dir+3)%4
    dist=int(walk[1:])
    for i in range(dist):
        px+=dirs[dir][0]
        py+=dirs[dir][1]
        if (px,py) in pset and first==False:
            print("First visit twice: ",px,py,abs(px)+abs(py))
            first=True
        pset.add((px,py))
print (abs(px)+abs(py))
