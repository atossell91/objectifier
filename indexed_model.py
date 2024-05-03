from vertex import vertex
from vector_dict import vector_dict
from indexed_vertex import indexed_vertex

class indexed_model:
    def __init__(self, positions, normals, indices):
        self.positions = positions
        self.normals = normals
        self.vertices: list[indexed_vertex] = indices

def index_model(vertices: list[vertex]):
    position_map: vector_dict = vector_dict()
    normal_map: vector_dict = vector_dict()
    indexes: list[indexed_vertex] = []

    for v in vertices:
        pos: int = position_map.add_or_retreive(v.position)
        norm: int = normal_map.add_or_retreive(v.normal)
        iv = indexed_vertex(pos, norm)
        indexes.append(iv)
    
    model: index_model = indexed_model(position_map.to_list(), normal_map.to_list(), indexes)
    return model

def padv(number, amt=8):
    if number < 0:
        return str(number).ljust(amt+1, '0')
    else:
        return str(number).ljust(amt, '0')

def padn(number, amt=7):
    return str(number)

def model_to_obj(model: index_model, path, scale=1) -> str:
    with open(path, 'w') as file:
        for pos in model.positions:
            file.write(f'v {padv(pos.X * scale)} {padv(pos.Z * scale)} {padv(-pos.Y * scale)}\n')

        for norm in model.normals:
            file.write(f'vn {padn(norm.X * scale, 6)} {padn(norm.Z, 6)} {padn(norm.Y, 6)}\n')

        face = []
        for vert in model.vertices:
            face.append(vert)
            if len(face) == 3:
                file.write('f ')
                for v in face:
                    file.write(f'{v.vertex + 1}//{v.normal + 1} ')
                file.write('\n')
                face.clear()
            
