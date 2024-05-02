class vector3D:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
    
    def __str__(self):
        return f'({self.X}, {self.Y}, {self.Z})'
