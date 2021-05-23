from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("Enter what you would like to draw (Rectangle, Square or Quit): ")

    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_red = int(input("Enter a value for the red color (0 to 255): "))
        rec_green = int(input("Enter a value for the green color (0 to 255): "))
        rec_blue = int(input("Enter a value for the blue color (0 to 255): "))

        # Create the rectangle
        rectangle = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height,
                              color=(rec_red, rec_green, rec_blue))
        rectangle.draw(canvas=canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length of the square: "))
        sqr_red = int(input("Enter a value for the red color (0 to 255): "))
        sqr_green = int(input("Enter a value for the green color (0 to 255): "))
        sqr_blue = int(input("Enter a value for the blue color (0 to 255): "))

        # Create the square
        square = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(sqr_red, sqr_green, sqr_blue))
        square.draw(canvas=canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("files/canvas.png")
