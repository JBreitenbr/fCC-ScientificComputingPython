class Rectangle:
  def __init__(self,width,height):
      self.width=width
      self.height=height

  def set_width(self,width):
      self.width=width

  def set_height(self,height):
      self.height=height

  def get_area(self):
      return self.width*self.height

  def get_perimeter(self):
      return 2*(self.width+self.height)

  def get_diagonal(self):
      return (self.width**2+self.height**2)**0.5
  def __str__(self):
      return "Rectangle(width={}, height={})".format(self.width,self.height)

  def get_picture(self):
      if self.width>50 or self.height>50:
        return "Too big for picture."
      return ('*'*self.width+"\n")*self.height

  def get_amount_inside(self,shape):
      max_width=self.width // shape.width
      max_height=self.height // shape.height
      return max_width*max_height

class Square(Rectangle):
  def __init__(self,len):
      super().__init__(len,len)
    
  def __str__(self):
      return "Square(side={})".format(self.width)
    
  def set_side(self,len):
      self.width=len
      self.height=len

  def set_width(self,len):
      self.width=len
      self.height=len

  def set_height(self,len):
      self.width=len
      self.height=len
    
