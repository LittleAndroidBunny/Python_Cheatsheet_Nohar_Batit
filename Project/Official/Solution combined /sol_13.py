import random
import numpy
def f1(x,y,z):
    div=1
    for i in range (2,max(x,y,z)):
        if (x%i==0 and y%i==0 and z%i==0 and i>div):
            div=i
    return div
# print (f1(30,15,90))
comp1="O(n)"

def f2(l1,l2,l3):
    l=[]
    for i in l1:
        if (i in l2 and i not in l3) or (i in l3 and i not in l2):
            l.append(i)
    for i in l2:
        if (i in l3 and i not in l1) or (i in l1 and i not in l3):
            l.append(i)
    return l
# l1=[2,3,4,5,6,7]
# l2=[3,4,5,6,7,8]
# l3=[2,3,4,12,13,14]
# print (f2(l1,l2,l3))

def f3(x):
      
    low = min(-1.0, x) # if you're not familiar with "min" you can do it with "if"
    high = max(1.0, x) # if you're not familiar with "max" you can do it with "if"
    ans = (high + low)/2.0 
    while abs(ans**5 - x) >=-x/1000000 : 
        if ans**5 < x: 
            low = ans 
        else: 
            high = ans 
        ans = (high + low)/2.0 
    return ans
# print (f3(-445568787))

def f4(d1,d2):
    d={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    for i in range (10):
        for j in d1[i]:
            if j in d2[i]:
                d[i].append(j)
    return (d)
# d1={0:[],1:[12,15],2:[223,2456],3:[3456,3333],4:[],5:[],6:[],7:[],8:[],9:[]}
# d2={0:[],1:[12,13],2:[],3:[3333],4:[45678,44],5:[],6:[],7:[],8:[],9:[]}
# print (f4(d1,d2))
class c5(object):
    def __init__(self,a,color):
        assert (type(a)==float or type(a)==int) and (color=="blue" or color=="red"), "str" 
        self.a=a
        self.color=color
    def area(self):
        return (self.a)**2
    def __str__(self):
        string=str(self.a)+","+self.color
        return (string)
    def __add__(self,other):
        sum_a=(self.a**2+other.a**2)**0.5
        sum_color="red"
        if self.color=="blue" or other.color=="blue":
            sum_color="blue"
        return c5(sum_a,sum_color)
# a=c5(4,"blue")
# b=c5(5,"blue")
# print ((a+b))
class c5b(c5):
    def __init__(self,a,color):
        assert a==int(a)
        c5.__init__(self,a,color)
    def __add__(self,other):
        if type(other)==c5b and ((self.a**2+other.a**2)**0.5)==int((self.a**2+other.a**2)**0.5):
            sum_a=(self.a**2+other.a**2)**0.5
            sum_color="red"
            if self.color=="blue" or other.color=="blue":
                sum_color="blue"
            
            return c5b(sum_a,sum_color)
        else: 
            return c5.__add__(self,other)
# a=c5b(4,"blue")
# b=c5b(5,"blue")
# c=c5b(3,"red")
# print(a+b)
# print(a+c)
# print (type(a+b))
# print (type(a+c))
def f6(n):
    random.seed(1)
    goal=0
    for i in range (10000):
        result=0
        for j in range (n):
            if random.choice([0,1])==1:
                result+=1
        if result==n/2:
            goal+=1
    return(goal/10000)
# print (f6(100))
def f7a(l):
    l1=[]
    l2=[]
    for i in l:
        l1.append(i[1])
        l2.append(i[2])
    mean1,mean2=numpy.mean(l1),numpy.mean(l2)
    std1,std2=numpy.std(l1),numpy.std(l2)
    for j in l:
        j[1],j[2]=(j[1]-mean1)/std1,(j[2]-mean2)/std2
    return l
# L=[[12,34,23,45],["re",45,32],["do",22,33]]

# print (f7a(L))
# def f7b(t,l):
def f7b(t,L):
    def dis(l1,l2):
        return ((l1[1]-l2[1])**2+(l1[2]-l2[2])**2)**(1/2)
    L1=L[:]
    l=L1[0]
    L2=[]
    for j in range (3):
        for i in L1:
            if dis(t,i)<dis(t,l):
                l=i
        L2.append(i)
        L1.remove(i)
    return L2
def f7c(t,L):
    L2=f7b(t,L)
    sum=0
    for i in L2:
        sum=+i[3]
        print (sum)
    if sum>1:
        t.append(1)
    else:
        t.append(0)
    return (t)
# L=[["Avi",12,43,0],["Beni",21,23,1],["Kobi",11,23,0],["Meni",12,12,1],["Shlomi",22,4,1],
# ["Ben",13,15,0],["Yoni",25,23,1],["Moti",16,16,0],["Tomer",18,12,1]]
# Lc=(f7a(L))
# t=["Hezi",0.5,0.9]
# print(f7c(t,Lc))
            
        
        
    
def f8(n):
    if n==1 or n==2:
        return n
    return n*f8(n-2)
# print (f8(5))

        
        
        
    