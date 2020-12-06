num=0
num2=0
for line in open("input07.txt",'r').readlines():
    mod=True
    enable=False
    block=False
    for c in enumerate(line):
        mod=mod and c[1]!='['
        mod=mod or c[1]==']'
        ind=c[0]
        if ind>2:
            if line[ind-3]==line[ind] and line[ind-2]==line[ind-1] and line[ind-3]!=line[ind-2]:
                if mod:
                    enable=True
                else:
                    block=True
    if enable and not block:
        num+=1
print(num)
   
num=0
for line in open("input07.txt",'r').readlines():
    mod=True
    aba=set()
    bab=set()
    for c in enumerate(line):
        mod=mod and c[1]!='['
        mod=mod or c[1]==']'
        ind=c[0]
        if ind>1:
            if line[ind-2]==line[ind] and line[ind-1]!=line[ind]:
                if mod:
                    aba.add((line[ind-1],line[ind]))
                else:
                    bab.add((line[ind],line[ind-1]))
    if len(aba.intersection(bab))>0:
        num+=1
print(num)
