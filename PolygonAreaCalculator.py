class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.set_width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**5
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    

    def get_picture(self):
        # returns a string representation
        # of the rectangle
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        rectangle = '*'*(self.width + 2) + '\n'
        for i in range(self.height - 4):
            rectangle += '*' + ' '*self.width + '*' + '\n'
        rectangle += '*'*(self.width - 2)
        return rectangle
    
    def get_amount_inside(self, shape2):
        # calculat the times that a specified rectangle fits inside of anthor shape
        if not isinstance(self.shape, (Square, Rectangle)) or not isinstance(shape2, (Square, Rectangle)):
            raise ValueError("Both arguments must be instances of Square or Rectangle")
        return self.shape.area() // shape2.area()



class Square(Rectangle):
    # inheritance
    def __init__(self, side):
        super().__init__(side, side)
        self.side_width = side

    def set_side(self, side):
        self.side_width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_height(height)

    def __str__(self):
        return f'Square(side={self.set_side})'