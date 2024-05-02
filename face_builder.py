from face import face
from vertex import vertex

class face_builder:
    def __init__(self):
        self.vertices_per_face: int = 3
        self.vertices = []

    def add_vertex(self, vert: vertex) -> None:
        if len(self.vertices) > self.vertices_per_face:
            raise Exception("Too many vertices!")
        
        self.vertices.append(vert)

    def is_complete(self) -> bool:
        return len(self.vertices) == self.vertices_per_face
    
    def flush_face(self) -> face:
        f = face(self.vertices)
        self.vertices.clear()
        return f
