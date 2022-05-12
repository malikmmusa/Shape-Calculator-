import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_diagonal(self):
    return  ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50: return "Too big for picture."
    return (('*' * self.width) + '\n') * self.height

  def get_amount_inside(self, shape):
    return math.floor((self.width * self.height) / (shape.width * shape.height))

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'
    
  def set_side(self, side):
    self.width = self.height = side
    
  def set_height(self, height):
    self.set_side(height)

  def self_width(self, width):
    self.set_side(width)

    