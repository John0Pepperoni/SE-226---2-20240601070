x1 = int(input("Enter x coordinate for first point"))
y1 = int(input("Enter y coordinate for first point"))

x2 = int(input("Enter x coordinate for second point"))
y2 = int(input("Enter y coordinate for second point"))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)