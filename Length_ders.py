class Length():
    metric = {"mm":0.001,"cm": 0.01,"m": 1,"km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
                   "mi": 1609.344}
    def __init__(self,value, unit="m"):
        self.value=value
        self.unit=unit
    def convertToMeters(self):
        return self.value*Length.metric[self.unit]
    def __add__(self, other):
        if type(other)==int or type(other)==float:
            l=self.convertToMeters() + other
        else:
            l=self.convertToMeters()+other.convertToMeters()
        return Length(l/Length.metric[self.unit],self.unit)
    def __iadd__(self, other):
        if type(other)==int or type(other)==float:
            l=self.convertToMeters() + other
        l = self.convertToMeters() + other.convertToMeters()
        self.value=l/Length.metric[self.unit]
        return self
    def __radd__(self, other):
        if type(other)==int or type(other)==float:
            l=self.convertToMeters()+other
        else:
            l=self.convertToMeters() + other.convertToMeters
        return  Length(l/Length.metric[self.unit],self.unit)
    def __str__(self):
        return str(self.convertToMeters())
    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"

#len1=Lenght(100,"cm")--- 100*0.01--- 100*metric["cm"]
len1=Length(200,"cm")#print(len1.convertToMeters())
len2=Length(30,"km")
print(Length(200,"cm") +Length(30,"km") )
x=Length(4000,"km")
x+=Length(400)
print(x)
print(4 + Length(56,"cm") )
