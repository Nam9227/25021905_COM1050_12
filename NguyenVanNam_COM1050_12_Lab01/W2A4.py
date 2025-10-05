s=input()
a=s.split(" ")
b=[0]
for i in a:
    b.append(int(i))
print(round((((b[1]+b[2]+b[3])+(b[4]+b[5])*2+b[6]*3)/10),1))