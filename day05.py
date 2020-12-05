import hashlib 
id='wtnhxymk'
#id='abc'
key=''
key2=list('_'*8)
n=0
i=0
while i<8:
    string=id+str(n)
    while hashlib.md5(string.encode()).hexdigest()[:5]!='00000':
        n+=1
        string=id+str(n)
    hash=hashlib.md5(string.encode()).hexdigest()
    key+=hash[5]
    if hash[5]<'8' and key2[int(hash[5])]=='_':
        key2[int(hash[5])]=hash[6]
        i+=1
    print(n,key,hashlib.md5(string.encode()).hexdigest(),key2)
    n+=1
print(key[:8],''.join(key2))

