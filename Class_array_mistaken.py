class Human:

    def __init__(self,name):
        self.name =name
        self.names = []
    def add_name(self,fname):
        self.names.append(fname)

d=Human("Millan")
e=Human("Milu")
d.add_name("First name")
e.add_name("Last name")
print(d.names)
print(e.names)