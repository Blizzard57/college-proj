import sys
def UniqueSort(x):
    z=x.split(", ")
    p=set()
    n=len(z)
    for i in range(0,n):
        p.add(z[i])
    q=sorted(p)
    print(", ".join(q))
s=sys.argv[1]
for i in range(2,len(sys.argv)):
    s+=" " + sys.argv[i]
UniqueSort(s)
