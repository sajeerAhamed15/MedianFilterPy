def midValue(a):
    b=a.copy()
    b.sort()
    return ( b[(len(b)-1)//2] + b[(len(b))//2] ) / 2





f = open("route.txt", "r")
o = open("filtered_route.txt", "w+")

tune=5

a=list()
b=list()
for line in f:
    num=line.split(', ',1)
    a.append(float(num[0]))
    b.append(float(num[1]))
    if len(a)>tune:
        a.pop(0)
    if len(b)>tune:
        b.pop(0)
    print (str(midValue(a))+', '+str(midValue(b)))
    o.write(str(midValue(a))+', '+str(midValue(b))+'\n')


f.close()
o.close()




