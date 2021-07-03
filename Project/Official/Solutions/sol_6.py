#1.
print ("Answer 01")
def func(L):
    for i in L:
        if i%3==0:
            return i
    raise ValueError("There is no number divided by 3")
L=[2,4,3]
L2=[4,6,8]
print(func(L))
print(func(L2))
#2.
print ("Answer 02")
class EquilateralTriangle(object):
    def __init__(self,length):
        self.side=length
    def circumference(self):
        return 3*self.side
    def area(self):
        return (self.side**2)*(3**0.5)/2
    def __str__(self):
        return ("T<"+str(self.side)+">")
#3.
print ("Answer 03")
class Alient(object):

    try:
        def __init__(self, name, color):
            """ name is a string made of two small letters, color is "blue", "yellow" or "red" """
            assert (type(name) == str and len(name)==2 and name[0] in
            "abcdefghijklmnopqrstuvwxyz" and
            name[1] in "abcdefghijklmnopqrstuvwxyz" and
            ((color)=="blue" or color=="yellow" or color=="red")), "This in not an alient data"
            self.name = name
            self.color = color
        def get_name(self):
            return str(self.name)
        def get_color(self):
            return str(self.color)
        def set_name(self,newname):
            self.name=newname
        def set_color(self,newcolor):
            self.color=newcolor
        def __str__(self):
            return ( "alient:"+str(self.name)+":"+str(self.color))
    except:
        pass
#4.
print ("Answer 04")
def __add__(self, other):
    """ merging two alients """
    addname=self.name[0]+other.name[0]
    if (self.color=="blue" and other.color=="yellow") or (self.color=="yellow" and other.color=="blue"):
        addcolor="red"
    elif (self.color=="blue" and other.color=="red") or (self.color=="red" and other.color=="blue"):
        addcolor="yellow"
    elif (self.color=="yellow" and other.color=="red") or (self.color=="red" and other.color=="yellow"):
        addcolor="blue"
    else:
        addcolor=self.color
    return Alient(addname,addcolor)
