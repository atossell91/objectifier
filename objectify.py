import sys
from stl_reader import read_stl
from indexed_model import index_model
from indexed_model import indexed_model
from indexed_model import model_to_obj

from vector3D import vector3D

def get_follower(args, arg_name):
    for i in range(len(args)):
        if args[i] == arg_name and i + 1 < len(args):
            return args[i+1]
    return None

def get_input_path(args):
    return get_follower(args, '-i')

def get_output_path(args):
    return get_follower(args, '-o')

def get_scale(args):
    return get_follower(args, '-scale')

def main():
    input_path = get_input_path(sys.argv)
    output_path = get_output_path(sys.argv)
    #scaleStr = get_scale(sys.argv)

    if output_path is None:
        output_path = input_path[:-3] + ".obj"

    vertices = read_stl(input_path)
    model: indexed_model = index_model(vertices)

    model_to_obj(model, output_path, scale=0.001)

if __name__ == '__main__':
    main()