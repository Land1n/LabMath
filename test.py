l = [1,2,3,4,5]
v = [6,7,8]
t = []

t = [[] for i in max(l,v,key=len)]

for i in [l,v]:
    for j,el2 in enumerate(i):
        t[j].append(el2)    


# for i in t:

print(t)