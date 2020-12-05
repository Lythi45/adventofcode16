su=0
for room in open("input04.txt",'r').readlines():
    parts=room.split('[')
    check=parts[1][:-2]
    na=parts[0].split('-')
    name=''.join(na[:-1])
    dname=' '.join(na[:-1])
    id=int(na[-1])
    cd={}
    for c in name:
        cd[c]=cd.get(c,0)+1
    
    sort_c=sorted([x[::-1] for x in cd.items()],key=lambda x:x[1])
    sort_c=sorted(sort_c,key=lambda x:x[0],reverse=True)[:5]
    check2=''.join([x[1] for x in sort_c])

    if check==check2:
        su+=id
    dec_name=''
    for c in dname:
        dec_name+=chr((ord(c)-ord('a')+id)%26+ord('a')) if c!=' ' else ' '
    if dec_name.find('northpole')>=0:
        print(dec_name,id)

print(su)



