import re
from vector3D import vector3D
from vertex import vertex

number_pattern: str = '-?\d+'
vertex_pattern: str = f'\s*vertex(\s+{number_pattern})+'
normal_pattern: str = f'\s*facet\s+normal(\s+{number_pattern})+'

index_x: int = 0
index_y: int = 1
index_z: int = 2

def is_number(str: str) -> bool:
    m = re.match(number_pattern, str)
    return m != None
    

def is_vertex(line: str) -> bool:
    m = re.match(vertex_pattern, line)
    return m != None

def is_normal(line: str) -> bool:
    m = re.match(normal_pattern, line)
    return m != None

def extract_nums(line: str):
    tokens = line.split()
    
    nums = []
    
    for token in tokens:
        if is_number(token):
            nums.append(float(token))
    
    return nums
    
def read_stl(path: str):

    vertices = []

    with open(path, 'r') as file:
        
        normal: vector3D = None

        for line in file:
            if is_vertex(line):
                nums = extract_nums(line)
                position: vector3D = vector3D(
                    nums[index_x],
                    nums[index_y],
                    nums[index_z]
                )

                vert: vertex = vertex(position, normal)
                vertices.append(vert)

            if is_normal(line):
                nums = extract_nums(line)
                normal = vector3D(
                    nums[index_x],
                    nums[index_y],
                    nums[index_z]
                )

    return vertices
