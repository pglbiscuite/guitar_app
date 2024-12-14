from scales import *


#   Converting The en_scale to the ro_scale
def ro_scale_convertor(en_scale, ro_scale):
    return list(map(lambda x: ro_scale[x], range(len(en_scale))))
