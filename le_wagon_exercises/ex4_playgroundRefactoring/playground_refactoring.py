
def circle_math(radius):
    return [3.141592653589793*(radius*2), 3.141592653589793*(radius*radius)]

print(circle_math(3))

values = circle_math(5)
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")