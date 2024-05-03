class vector3D:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
    
    def __str__(self):
        return f'({self.X}, {self.Y}, {self.Z})'
    
    def __lt__(self, other: 'vector3D'):
        if self.X != other.X:
            return self.X < other.X
        elif self.Y != other.Y:
            return self.Y < other.Y
        elif self.Z != other.Z:
            return self.Z < other.Z
        else:
            return False
    
    def __gt__(self, other: 'vector3D'):
        if self.X != other.X:
            return self.X > other.X
        elif self.Y != other.Y:
            return self.Y > other.Y
        elif self.Z != other.Z:
            return self.Z > other.Z
        else:
            return False
        
    def __eq__(self, other: 'vector3D'):
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z
