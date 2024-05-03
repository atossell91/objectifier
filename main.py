from stl_reader import read_stl
from indexed_model import index_model
from indexed_model import indexed_model
from indexed_model import model_to_obj

from vector3D import vector3D
def main():
    vertices = read_stl('../modulus/stl/shop-window.stl')
    model: indexed_model = index_model(vertices)

    scale = 0.001

    model_to_obj(model, "./text.obj")

if __name__ == '__main__':
    main()