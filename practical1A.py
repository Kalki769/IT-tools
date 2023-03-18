class Reactangle:
    def calculateArea(self):
        self.l=float(input("Enter the length: "))
        self.b=float(input("Enter the breadth: "))
        print("Area of Reactangle is: ",self.l*self.b)

    def calculatePerimeter(self):
        perimeter= 2* (self.l+self.b)
        print("Perimeter of ractangle is: ",perimeter)

r=Reactangle()
r.calculateArea()
r.calculatePerimeter()
        
