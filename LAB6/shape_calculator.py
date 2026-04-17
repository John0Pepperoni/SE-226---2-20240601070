import geometry_utils

operation_dict = dict()
operation_dict = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")
print("Enter the operation you want to perform: ", end="")
operation = input()

if operation == "circle_area":
    radius = float(input("Enter the radius of the circle: "))
    print(operation_dict[operation](radius))

elif operation == "circle_perimeter":
    radius = float(input("Enter the radius of the circle: "))
    print(operation_dict[operation](radius))

elif operation == "rectangle_area":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(operation_dict[operation](length, width))

elif operation == "rectangle_perimeter":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(operation_dict[operation](length, width))

elif operation == "triangle_area":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(operation_dict[operation](base, height))

else:
    print("Invalid operation.")