from vector3D import vector3D

class vertex:
    def __init__(self, position: vector3D, normal: vector3D):
        self.position: vector3D = position
        self.normal: vector3D = normal