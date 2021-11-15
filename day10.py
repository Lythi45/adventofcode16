commands=[]
clist=[]

robots={}
output={}

for line in open("input10.txt",'r').readlines():
    clist.append(line.split())

for c in clist:
    if c[0]=="value":
        val=int(c[1])
        botn=int(c[5])
        robots[botn]=sorted(robots.get(botn,[])+[val])
    else:
        botn=int(c[1])
        low=int(c[6])
        high=int(c[11])
        commands.append((botn,c[5],low,high))
    

loop=True
while loop:
    loop=False
    for c in commands:
        botn=c[0]
        if botn in robots and len(robots[botn])==2:
            loop=True
            if robots[botn]==[17,61]:
                print(botn)
            if c[1]=="bot":
                robots[c[2]]=sorted(robots.get(c[2],[])+[robots[botn][0]])
            else:
                output[c[2]]=output.get(c[2],[])+[robots[botn][0]]
            robots[c[3]]=sorted(robots.get(c[3],[])+[robots[botn][1]])
            robots[botn]=[]
    
print(int(output[0][0])*int(output[1][0])*int(output[2][0]))




    