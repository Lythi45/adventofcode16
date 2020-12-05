walks=list(map(lambda s:s.strip(),open("input02.txt",'r').readlines()))
px=1
py=1
num=''
dirs={'D':(0,1),'R':(1,0),'U':(0,-1),'L':(-1,0)}
for walk in walks:
    for step in walk:
        dir=dirs[step]
        pxx=px+dir[0]
        pyy=py+dir[1]
        if pyy>=0 and pyy<3 and pxx>=0 and pxx<3:
            px=pxx
            py=pyy
    num+=str(1+px+py*3)
print(num)
    
chars="123456789ABCD"
pad="""
    1
  2 3 4
5 6 7 8 9
  A B C
    D"""
    
pad=pad.split('\n')

px=0
py=3
num=''
dirs={'D':(0,1),'R':(1,0),'U':(0,-1),'L':(-1,0)}
for walk in walks:
    for step in walk:
        dir=dirs[step]
        pxx=px+dir[0]*2
        pyy=py+dir[1]
        if pyy>0 and pyy<6 and pxx>=0 and pxx<len(pad[pyy]):
            if pad[pyy][pxx] in chars:
                px=pxx
                py=pyy
    num+=pad[py][px]
print(num)
