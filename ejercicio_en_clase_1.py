class Point:                                            # Class Point for the coordinate left_corner point
    definition: str = "It's the coordinate of a point in the Cartesian plane"  # Class attributes

    def __init__(self, x=0, y=0):                       # Instance attributes, class constructure
        self.x = x                                      # Initialize x
        self.y = y                                      # Initialize y

    def move(self, new_x, new_y):                       # Use to control modifications
        self.x = new_x
        self.y = new_y

    def reset(self):                                    # Use to control modifications
        self.x = 0
        self.y = 0

class Line:                                             # Class Line
    definition: str = "It's the geometric form of a Line in the Cartesian plane"  # Class attributes
    def __init__(self, start_point, end_point):      # Instance attributes, class constructure                         
        self.start_point = start_point 
        self.end_point = end_point                       

    def compute_length(self):                             
        self.length = (((self.end_point.x - self.start_point.x) ** 2) +
                       ((self.end_point.y - self.start_point.y) ** 2)) ** 0.5
        return self.length

    def compute_slope(self):                            
        self.slope_rad = (self.end_point.y - self.start_point.y) / (self.end_point.x - self.start_point.x)
        slope_deg = self.slope_rad * (180 / 3.1416)
        return slope_deg

    def compute_horizontal_cross(self):                            
        if self.start_point.x <= 0:
            if self.end_point.x <= 0:
                return False
            else: 
                return True
        elif self.end_point.x <= 0:
            if self.start_point.x <= 0:
                return False
            else: 
                return True
        else: return False

    def compute_vertical_cross(self):                            
        if self.start_point.y <= 0:
            if self.end_point.y <= 0:
                return False
            else: 
                return True
        elif self.end_point.y <= 0:
            if self.start_point.y <= 0:
                return False
            else: 
                return True
        else: return False

class Rectangle:                                        # Class Rectangle 
    definition: str = "It's the geometric form of a Rectangle in the Cartesian plane"  # Class attributes

    def __init__(self, method):     # Instance attributes, class constructure

        if method == 1:                                         # If its with the 1st method
            left_corner_x = float(input("Insert x component of the left corner point: "))
            left_corner_y = float(input("Insert y component of the left corner point: "))
            left_corner = Point(x=left_corner_x, y=left_corner_y)   

            width = float(input("Insert the width of the rectangle: "))
            height = float(input("Insert the height of the rectangle: "))

            self.left_corner = left_corner                  # Initialize left_corner
            self.width = width                              # Initialize width
            self.height = height                            # Initialize height

        elif method == 2:                                       # If its with the 2nd method
            center_point_x = float(input("Insert x component of the center point: "))
            center_point_y = float(input("Insert y component of the center point: "))

            width = float(input("Insert the width of the rectangle: "))
            height = float(input("Insert the height of the rectangle: "))

            left_corner_x = center_point_x - (width / 2)
            left_corner_y = center_point_y - (height / 2)
            left_corner = Point(x=left_corner_x, y=left_corner_y)

            self.left_corner = left_corner                  # Initialize left_corner
            self.width = width                              # Initialize width
            self.height = height                            # Initialize height

        elif method == 3:                                       # If its with the 3rd method
            left_corner_x = float(input("Insert x component of the left corner point: "))
            left_corner_y = float(input("Insert y component of the left corner point: "))
            left_corner = Point(x=left_corner_x, y=left_corner_y)

            right_corner_x = float(input("Insert x component of the right corner point: "))
            right_corner_y = float(input("Insert y component of the right corner point: "))

            width=right_corner_x-left_corner_x
            height=right_corner_y-left_corner_y

            self.left_corner = left_corner                  # Initialize left_corner
            self.width = width                              # Initialize width
            self.height = height                            # Initialize height

        elif method==4:                                         # If its with the 4th method         # If its with the 4th method
            lines = []
            for i in range(4):
                start_point_x = float(input("Insert x component of the start point of the line: "))
                start_point_y = float(input("Insert y component of the start point of the line: "))
                start_point = Point(x=start_point_x, y=start_point_y) 

                end_point_x = float(input("Insert x component of the end point of the line: "))
                end_point_y = float(input("Insert y component of the end point of the line: "))
                end_point = Point(x=end_point_x, y=end_point_y) 

                line = Line(start_point=start_point, end_point=end_point)
                lines.append(line)

            dot_products = [
                (lines[0].end_point.x - lines[0].start_point.x) * (lines[1].end_point.x - lines[1].start_point.x) +
                (lines[0].end_point.y - lines[0].start_point.y) * (lines[1].end_point.y - lines[1].start_point.y),

                (lines[1].end_point.x - lines[1].start_point.x) * (lines[2].end_point.x - lines[2].start_point.x) +
                (lines[1].end_point.y - lines[1].start_point.y) * (lines[2].end_point.y - lines[2].start_point.y),

                (lines[2].end_point.x - lines[2].start_point.x) * (lines[3].end_point.x - lines[3].start_point.x) +
                (lines[2].end_point.y - lines[2].start_point.y) * (lines[3].end_point.y - lines[3].start_point.y),

                (lines[3].end_point.x - lines[3].start_point.x) * (lines[0].end_point.x - lines[0].start_point.x) +
                (lines[3].end_point.y - lines[3].start_point.y) * (lines[0].end_point.y - lines[0].start_point.y)
            ]

            if all(dot_product == 0 for dot_product in dot_products):
                self.left_corner = Point(
                    x=min(min(line.start_point.x, line.end_point.x) for line in lines),
                    y=min(min(line.start_point.y, line.end_point.y) for line in lines)
                )
                self.width = max(max(line.end_point.x, line.start_point.x) for line in lines) - self.left_corner.x
                self.height = max(max(line.end_point.y, line.start_point.y) for line in lines) - self.left_corner.y
            else:
                print("Not a rectangle")

        else:
            print("No valid number")

    def compute_area(self):                             # Function for its area
        area = self.width * self.height
        return area

    def compute_perimeter(self):                        # Function for its perimeter
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def compute_interference_point(self, point: Point) -> bool:
        if (self.left_corner.x <= point.x <= self.left_corner.x + self.width) and (self.left_corner.y <= point.y <= self.left_corner.y + self.height):
            return True
        else:
            return False

class Square(Rectangle):                                # Class Square 
    definition: str = "It's the geometric form of a Square in the Cartesian plane"

    def __init__(self, rectangle: Rectangle):
        super().__init__(method)
        self.left_corner = rectangle.left_corner
        self.width = rectangle.width

# Method

print("Insert 1 if your method to initialize the rectangle is with the left_corner, width, and height")     # Select the method to inicialice
print("Insert 2 if your method to initialize the rectangle is with the center_point, width, and height")
print("Insert 3 if your method to initialize the rectangle is with two opposite corners")
print("Insert 4 if your method to initialize the rectangle with 4 lines")
method = int(input(": "))

# Rectangle

print("\nFor the Rectangle") 

rectangle_1 = Rectangle(method)
print(rectangle_1.compute_area())
print(rectangle_1.compute_perimeter())

# Square

print("\nFor the Square") 

square_1 = Square(rectangle_1)
print(square_1.compute_area())
print(square_1.compute_perimeter())

print("\n") 

# Verification point

point_x = float(input("Insert x component of the point you want to know if it's inside the rectangle: "))
point_y = float(input("Insert y component of the point you want to know if it's inside the rectangle: "))
verify_point = Point(point_x, point_y)

print("\n") 

print(rectangle_1.compute_interference_point(verify_point))

# Verification line

print("\n") 

start_point_x = float(input("Insert x component of the start point of the line: "))
start_point_y = float(input("Insert y component of the start point of the line: "))
start_point = Point(x=start_point_x, y=start_point_y) 

end_point_x = float(input("Insert x component of the end point of the line: "))
end_point_y = float(input("Insert y component of the end point of the line: "))
end_point = Point(x=end_point_x, y=end_point_y) 

print("\nFor the Line") 

line = Line(start_point=start_point, end_point=end_point)
print(line.compute_length())
print(line.compute_slope())
print(line.compute_horizontal_cross())
