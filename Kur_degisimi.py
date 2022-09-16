"""
class Ccr():
    currencies = {'CHF': 1.0821202355817312,
                  'CAD': 1.488609845538393,
                  'GBP': 0.8916546282920325,
                  'JPY': 114.38826536281809,
                  'EUR': 1.0,
                  'USD': 1.11123458162018}
    def __init__(self,value,unit='EUR'):
        self.value=value
        self.unit=unit
    def changeTo(self,new_unit):
        self.value=self.value/Ccr.currencies[self.unit]*Ccr.currencies[new_unit]
        self.unit=new_unit
    def __str__(self):
        return "{}, {}".format(self.value, self.unit)
    def __add__(self, other):
        if type(other)==int or type(other)==float:# Ccr(130,'JPY') +5
            x=other*Ccr.currencies[self.unit]
        else:#Ccr(130,'JPY') + Ccr(23,'CAD')
            x=(other.value/Ccr.currencies[other.unit])*Ccr.currencies[self.unit]
        return Ccr(self.value+x,self.unit)
    def __radd__(self, other):
        if type(other)==int or type(other)==float:# 5+Ccr(130,'JPY')
            x=other*Ccr.currencies[self.unit]
        else:#Ccr(130,'JPY') + Ccr(23,'CAD')
            x=(other.value/Ccr.currencies[other.unit])*Ccr.currencies[self.unit]
        self.value+=x
        return self
v1=Ccr(130,'JPY') # self.value=130  self.unit='JPY'
#print(v1)
#v1.changeTo('EUR') #new_unit=EUR
#print(v1)
v2=Ccr(85,'GBP')
y=Ccr(130,'JPY') + Ccr(85,'GBP')
print(y)
x=5+v1
print(x)
"""
"""
class Plist(list):
    def __init__(self, l):
        list.__init__(self, l)
    def push(self, item):
        self.append(item)
if __name__ == "__main__":
    x = Plist([3,4])
    x.push(40)
    print(x)
"""
"""
# __mul__ metodunun kullanımı
class Foo():
    def __init__(self,val):
        self.val=val
    def __str__(self):
        return "Foo[%s]"% self.val
class Bar():
    def __init__(self,val):
        self.val=val
    def __mul__(self, other):
        return Bar(self.val*other.val)
    def __rmul__(self, other):
        return Foo(self.val*other.val)
    def __str__(self):
        return "Bar[%s]"% self.val
#kod çağırma
f=Foo(5)
b=Bar(6)
print(f*b)
print(b*f)
"""
"""
class FoodSupply():
    def __call__(self,p1,p2):
        return "spam"
foo=FoodSupply() #örnek 1
bar=FoodSupply() #örnek 2
print(foo(),bar()) # call aracılığı ile örnekleri fonksiyon gibi kullanabiliyorum
"""
"""
class FoodSupply():
    def __init__(self,*incredients): #FoodSupply("pirinç","şeker","yag")
        self.incredients=incredients
    def __call__(self):
        result= " ".join(self.incredients) + " Lezzetli yiyecekler !"
        return result
f1=FoodSupply("kakao","süt","şeker","bal") # örnek 1
print(f1())
"""
"""
TriangleArea
- a, b, c kenar uzunlukları
"""
"""
class TriangleArea():
    def __call__(self,a,b,c):
        u=(a+b+c)/2
        result=(u*(u-a)*(u-b)*(u-c))**0.5
        return result
alan1=TriangleArea() #örnek oluşturdum
print(alan1(3,4,5)) 
#parametreleri örnek içerisine girdik
#örneğin fonksiyon gibi kullanılmasını __ call__ aracılığıyla sağladık
"""
# y=mx+b
#StaightLines sınıfı oluştur--- m:eğim ve b-y eksenini kestiği nokta
#call parametresi "x" olsun
#örnek çağırırken örnek1=StaightLines(3,4)---örnek1(100)
"""
class StraightLines():
    def __init__(self,m,b):
        self.m=m
        self.b=b
    def __call__(self,x):
        return self.m*x+self.b
örnek1=StraightLines(-10,5)
print(örnek1(0))
for x in range(-5,6):
    print(x,örnek1(x))
lines = []
lines.append(StraightLines(1, 0))
lines.append(StraightLines(0.5, 3))
lines.append(StraightLines(-1.4, 1.6))
from matplotlib import pyplot as plt
import numpy as np
X = np.linspace(-5,5,100)
for index, line in enumerate(lines):
    line = np.vectorize(line)
    plt.plot(X, line(X), label='line' + str(index))
plt.title('Some straight lines')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
"""