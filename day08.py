def extract_x_y(st,sep):
    print(st)
    return map(int,st.split(sep))

xs=50
ys=6
rows=[]
for row in range(ys):
    rows.append('.'*xs)

for line in open("input08.txt",'r').readlines():
    if line[:4]=="rect": 
        x,y=extract_x_y(line[5:],"x")
        print("rect",x,y)
        for r in range(y):
            rows[r]='#'*x+rows[r][x:]
    elif line[:10]=="rotate row":
        y,n=extract_x_y(line[13:]," by ")
        print("rrow",y,n)
        rows[y]=rows[y][-n:]+rows[y][:-n]
    elif line[:13]=="rotate column":
        x,n=extract_x_y(line[16:]," by ")
        print("rcolumn",x,n)
        nrows=[]
        for r in range(ys):
            nrows.append(rows[r][:x]+rows[(r-n+ys)%ys][x]+rows[r][x+1:])
        rows=nrows
    for r in range(ys):
        print(rows[r])

print(sum([len([c for c in row if c =='#']) for row in rows]))
