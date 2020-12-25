class Rectangle():
  def __init__(self, height, width):
    self.__height = height
    self.__width = width
    
  @property
  def area(self):    
    return self.__width * self.__height
  
  @property
  def width(self):
    return self.__width

  @width.setter
  def width(self, width):
    self.__width = width
    
    
  @property
  def height(self):
    return self.__height
  

rectangle1 = Rectangle(3, 5)
rectangle2 = Rectangle(5, 7)
print(rectangle1.area)
print(rectangle2.area)

print(rectangle1.width)
rectangle1.width = 9
print(rectangle1.width)
print(rectangle1.area)

print(rectangle2.__height)
  