class a:
    def display(self):
        print("Hello from class a")

class b(a):
    def display(self):
        print("Hello from class b")

class c(a):
    def display(self):
        print("Hello from class c")

class d(b, c):
    pass

v=d()
v.display()  # This will call the display method from class b due to MRO

