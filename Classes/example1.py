class University:
    
    def __init__(self,name,fullname):
        self.name = name
        self.fullname = fullname
 
    def print_name(self):
        print(self.name)
    
    def print_fullname(self):
        print(self.fullname)
        
    def set_name(self, name):
        self.name = name
        
    def set_fullname(self,fullname):
        self.fullname = fullname

def newName():
    name = input("Podaj skrót nazwy uniwersytetu: ")
    fullname = input("Podaj pełną nazwę uniwersytetu: ")
    return(name,fullname)

u1 = University(newName())
u1.print_name()

