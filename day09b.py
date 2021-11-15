def extract_x_y(st,sep):
    return map(int,st.split(sep))

input="".join(map(lambda x:x.strip(),open("input09.txt",'r').readlines()))
#input="(27x12)(20x12)(13x14)(7x10)(1x12)A"

def len_decompressed(input,start,end):
    n=0
    p=start
    while p<end:
        if input[p]=='(':
            clp=input.find(')',p+1)
            length,rep=extract_x_y(input[p+1:clp],'x')
            n+=len_decompressed(input,clp+1,clp+1+length)*rep
            p=clp+1+length
        else:
            n+=1
            p+=1
    return n

print(len_decompressed(input,0,len(input)))
