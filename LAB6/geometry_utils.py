def circle_area(radius):
    if radius <= 0:
        print("Invalid argument")
        exit()
    else:
        return 3.14 * radius * radius

def circle_perimeter(radius):
    if radius <= 0:
        print("Invalid argument")
        exit()
    else:
        return 2 * 3.14 * radius

def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid argument(s)")
        exit()
    else:
        return length * width

def rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        print("Invalid argument(s)")
        exit()
    else:
        return 2 * (length + width)

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        print("Invalid argument(s)")
        exit()
    else:
        return (base*height)/2