import re

number_pattern = '-?\d+'
vertex_pattern = f'\s*vertex(\s+{number_pattern})+'
normal_pattern = f'\s*facet\s+normal(\s+{number_pattern})+'

def is_number(str):
    m = re.match(number_pattern, str)
    return m != None
    

def is_vertex(line):
    m = re.match(vertex_pattern, line)
    return m != None

def is_normal(line):
    m = re.match(normal_pattern, line)
    return m != None

def extract_nums(line: str):
    tokens = line.split()
    
    nums = []
    
    for token in tokens:
        if is_number(token):
            nums.append(int(token))
    
    return nums
    
def read_stl(path):

    with open(path, 'r') as file:
        for line in file:
            if is_vertex(line):
                print(extract_nums(line))
            if is_normal(line):
                pass