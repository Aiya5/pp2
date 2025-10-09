import math

#Convert degree to radian-------------------------------------------------------------------------------------
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

#Area of a trapezoid--------------------------------------------------------------------------------------------------
height = 5
base1 = 5
base2 = 6
trapezoid_area = 0.5 * (base1 + base2) * height
print("Area of trapezoid:", trapezoid_area)

#Area of a regular polygon---------------------------------------------------------------------------------------
n = 4   # number of sides
s = 25  # length of a side
polygon_area = (n * s**2) / (4 * math.tan(math.pi / n))
print("Area of polygon:", round(polygon_area, 2))

#Area of a parallelogram-------------------------------------------------------------------------
base = 5
height_p = 6
parallelogram_area = base * height_p
print("Area of parallelogram:", parallelogram_area)
