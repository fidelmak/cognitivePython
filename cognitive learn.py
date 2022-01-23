import matplotlib.pyplot as plt

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
#RedCircle = Circle(10, 'red')
#print('Radius of object:',RedCircle.radius)
#RedCircle.add_radius(2)
#print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
#RedCircle.add_radius(5)
#print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
BlueCircle = Circle(radius=100)
print("bluecircle is: ",BlueCircle.radius)
print("the color is:",BlueCircle.color)
print("this is the output :",BlueCircle.drawCircle())