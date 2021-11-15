def extract_x_y(st,sep):
    return map(int,st.split(sep))

input="".join(map(lambda x:x.strip(),open("input09.txt",'r').readlines()))
#input="X(8x2)(3x3)ABCY"
n=0
output=""
while n<len(input):
    if input[n]=='(':
        clp=input.find(')',n+1)
        length,rep=extract_x_y(input[n+1:clp],'x')
        output+=input[clp+1:clp+1+length]*rep
        n=clp+1+length
    else:
        output+=input[n]
        n+=1
print(output)
print(len(output))
