def midValue(a):
    b=a.copy()
    b.sort()
    return ( b[(len(b)-1)//2] + b[(len(b))//2] ) / 2





f = open("route.txt", "r")
o = open("filtered_route.txt", "w+")

tune=5

a=list()
for line in f:
    a.append(float(line))
    if len(a)>tune:
        a.pop(0)
    print (a,midValue(a))



f.close()
o.close()




