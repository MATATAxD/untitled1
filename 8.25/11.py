a=[[1,2],[3,4],[5,6]]
b=[]
for i in a:
    for j in i:
     if j not in b:
        b.append(j)
print(b)
