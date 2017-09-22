import pandas as pd
import os


def import_matprops(mat):
    matprops = pd.read_csv(os.path.join(os.path.dirname(__file__), "materials.csv"), index_col=0)
    mat = matprops[mat]
    return mat


def material(mat):
    mat = import_matprops(mat)
    exp = "not found"
    data = {}
    data['info'] = "an unConventional project"

    #TODO differnetiate material type(isotropc,orthotropic,fiber....)
    data['data'] = {}
    #data['data']['material'] = mat.name
    data['data']['type'] = mat.type
    data['data']['density'] = mat.density
    data['data']['tensile_strength'] = mat.F1t
    data['data']['shear_strength'] = exp
    data['data']['shear_modulus'] = mat.G12
    data['data']['poisson_ratio'] = mat.nu12
    data['data']['youngs_modulus'] = mat.E1
    data['source'] = "#reference"

    return data

if __name__ == '__main__':
    print(material('steel'))
#TODO Handle  NaN
