"""
class Foo(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return "Foo [% s]" % self.val
class Bar(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return "Bar [% s]" % self.val
# Driver Code
f = Foo(5)
b = Bar(6)
print(f*b) #TypeError: unsupported operand type(s) for *: 'Foo' and 'Bar'
"""
#Lets add the __mul__ method in Foo class.
"""
class Foo(object):
    def __init__(self, val):
        self.val = val
    def __mul__(self, other):
        return Foo(self.val * other.val)
    def __str__(self):
        return "Foo [% s]" % self.val
class Bar(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return "Bar [% s]" % self.val
# Driver Code
f = Foo(5)
b = Bar(6)
print(f*b)
"""
#Let’s take the above example with a small modification
"""
class Foo(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return "Foo [% s]" % self.val
class Bar(object):
    def __init__(self, val):
        self.val = val
    def __rmul__(self, other):
        return Bar(self.val * other.val)
    def __str__(self):
        return "Bar [% s]" % self.val
# Driver code
f = Foo(5)
b = Bar(6)
print(f*b)
"""
#Lets modify the code again
class Foo(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return "Foo [% s]" % self.val
class Bar(object):
    def __init__(self, val):
        self.val = val
    def __rmul__(self, other):
        return Bar(self.val * other.val)
    def __mul__(self, other):
        return self.__rmul__(other)
    def __str__(self):
        return "Bar [% s]" % self.val
# Driver Code
f = Foo(5)
b = Bar(6)
print(b * f)
print(f * b)
