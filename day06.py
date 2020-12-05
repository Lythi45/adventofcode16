mess=open("input06.txt",'r').readlines()

for order in [True,False]:
    corr_mess=''
    for i in range(len(mess[0])):
        cd={}
        for c in [mess[j][i] for  j in range(len(mess))]:
            cd[c]=cd.get(c,0)+1
        most_c=sorted(cd.items(),key=lambda x:x[1],reverse=order)[0][0]
        corr_mess+=most_c

    print(corr_mess)