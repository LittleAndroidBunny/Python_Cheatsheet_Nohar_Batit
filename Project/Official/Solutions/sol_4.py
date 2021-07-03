
### Q1 ### :

def Tuples_scanner (t1,t2):
    result = ()
    for i in t1 :
        if i in t2 and i not in result:
            result = result +(i,)
    return result


### Q4 ### :

def Q4 (l,x,y):
    c = 0
    for i in l :
        if i > min(x,y) and i < max(x,y) :
            c+=1
    return c


def Q5 (l1,l2,l3):
    l = []
    for a in l1 :
        if a in l2 and a in l3 :
            l.append(a)
    return l