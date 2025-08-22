class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Length of side must be greater than 0")
            super().__setattr__(key, value)

        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be in the range 0 - 180 degrees")
            super().__setattr__(key, value)
            super().__setattr__('angle_b', 180 - value)

        elif key == "angle_b":
                raise ValueError("It is impossible to specify angle_b, It is automatically calculated from angle_a")
        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f"Rhombus: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"

figure = Rhombus(15, 60)
print(figure.side_a)
print(figure.angle_a)
print(figure.angle_b)
print(figure)