Classes and Objects in Python
Estimated time needed: 40 minutes

Objectives
After completing this lab you will be able to:

Work with classes and objects
Identify and define attributes and methods
Table of Contents
Introduction to Classes and Objects
Creating a class
Instances of a Class: Objects and Attributes
Methods
Creating a class
Creating an instance of a class Circle
The Rectangle Class
Introduction to Classes and Objects
Creating a Class
The first step in creating a class is giving it a name. In this notebook, we will create two classes: Circle and Rectangle. We need to determine all the data that make up that class, which we call attributes. Think about this step as creating a blue print that we will use to create objects. In figure 1 we see two classes, Circle and Rectangle. Each has their attributes, which are variables. The class Circle has the attribute radius and color, while the Rectangle class has the attribute height and width. Let’s use the visual examples of these shapes before we get to the code, as this will help you get accustomed to the vocabulary.

Image
Figure 1: Classes circle and rectangle, and each has their own attributes. The class Circle has the attribute radius and colour, the class Rectangle has the attributes height and width.

Instances of a Class: Objects and Attributes
An instance of an object is the realisation of a class, and in Figure 2 we see three instances of the class circle. We give each object a name: red circle, yellow circle, and green circle. Each object has different attributes, so let's focus on the color attribute for each object.

Image
Figure 2: Three instances of the class Circle, or three objects of type Circle.

The colour attribute for the red Circle is the colour red, for the green Circle object the colour attribute is green, and for the yellow Circle the colour attribute is yellow.

Methods
Methods give you a way to change or interact with the object; they are functions that interact with objects. For example, let’s say we would like to increase the radius of a circle by a specified amount. We can create a method called add_radius(r) that increases the radius by r. This is shown in figure 3, where after applying the method to the "orange circle object", the radius of the object increases accordingly. The “dot” notation means to apply the method to the object, which is essentially applying a function to the information in the object.

Image
Figure 3: Applying the method “add_radius” to the object orange circle object.

Creating a Class
Now we are going to create a class Circle, but first, we are going to import a library to draw the objects:

import matplotlib.pyplot as plt
%matplotlib inline  
# Import the library
​
import matplotlib.pyplot as plt
%matplotlib inline  
The first step in creating your own class is to use the class keyword, then the name of the class as shown in Figure 4. In this course the class parent will always be object:

Image
Figure 4: Creating a class Circle.

The next step is a special method called a constructor __init__, which is used to initialize the object. The inputs are data attributes. The term self contains all the attributes in the set. For example the self.color gives the value of the attribute color and self.radius will give you the radius of the object. We also have the method add_radius() with the parameter r, the method adds the value of r to the attribute radius. To access the radius we use the syntax self.radius. The labeled syntax is summarized in Figure 5:

Image
Figure 5: Labeled syntax of the object circle.

The actual object is shown below. We include the method drawCircle to display the image of a circle. We set the default radius to 3 and the default colour to blue:

# Create a class Circle
​
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
Creating an instance of a class Circle
Let’s create the object RedCircle of type Circle to do the following:

RedCircle = Circle(10, 'red')
# Create an object RedCircle
​
RedCircle = Circle(10, 'red')
We can use the dir command to get a list of the object's methods. Many of them are default Python methods.

# Find out the methods can be used on the object RedCircle
​
dir(RedCircle)
We can look at the data attributes of the object:

# Print the object attribute radius
​
RedCircle.radius
# Print the object attribute color
​
RedCircle.color
We can change the object's data attributes:

# Set the object attribute radius
​
RedCircle.radius = 1
RedCircle.radius
We can draw the object by using the method drawCircle():

# Call the method drawCircle
​
RedCircle.drawCircle()
We can increase the radius of the circle by applying the method add_radius(). Let's increases the radius by 2 and then by 5:

# Use method to change the object attribute radius
​
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
Let’s create a blue circle. As the default colour is blue, all we have to do is specify what the radius is:

BlueCircle = Circle(radius=100)
# Create a blue circle with a given radius
​
BlueCircle = Circle(radius=100)
As before, we can access the attributes of the instance of the class by using the dot notation:

# Print the object attribute radius
​
BlueCircle.radius
BlueCircle.color
# Print the object attribute color
​
BlueCircle.color
We can draw the object by using the method drawCircle():

BlueCircle.drawCircle()
# Call the method drawCircle
​
BlueCircle.drawCircle()
Compare the x and y axis of the figure to the figure for RedCircle; they are different.

The Rectangle Class
Let's create a class rectangle with the attributes of height, width, and color. We will only add the method to draw the rectangle object:

# Create a new Rectangle class for creating a rectangle object
​
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
Let’s create the object SkinnyBlueRectangle of type Rectangle. Its width will be 2 and height will be 3, and the color will be blue:

# Create a new object rectangle
​
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
As before we can access the attributes of the instance of the class by using the dot notation:

# Print the object attribute height
​
SkinnyBlueRectangle.height 
# Print the object attribute width
​
SkinnyBlueRectangle.width
# Print the object attribute color
​
SkinnyBlueRectangle.color
We can draw the object:

# Use the drawRectangle method to draw the shape
​
SkinnyBlueRectangle.drawRectangle()
Let’s create the object FatYellowRectangle of type Rectangle:

# Create a new object rectangle
​
FatYellowRectangle = Rectangle(20, 5, 'yellow')
We can access the attributes of the instance of the class by using the dot notation:

# Print the object attribute height
​
FatYellowRectangle.height 
# Print the object attribute width
​
FatYellowRectangle.width
# Print the object attribute color
​
FatYellowRectangle.color
We can draw the object:

# Use the drawRectangle method to draw the shape
​
FatYellowRectangle.drawRectangle()
Exercises
Text Analysis 
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
freqOf - returns the frequency of the word passed in argument.
The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise.
Hint: Some useful functions are replace(), lower(), split(), count()
class analysedText(object):
    
    def __init__ (self, text):
        pass
    
    def freqAll(self):        
        pass
    
    def freqOf(self,word):
        pass
        
Execute the block below to check your progress.

import sys
​
sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}
​
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'
​
print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    
Click here for the solution