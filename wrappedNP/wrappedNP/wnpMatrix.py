#coding: utf-8

import numpy as np
from . import wnpConst as wnp
from . import wnpVec3 as v3
from . import wnpVec4 as v4

class Matrix4x4:
    def __init__(self,value=None,position=v3.Vector3(),scale=v3.Vector3(1.0,1.0,1.0),rotation=v4.Quaternion(1,0,0,0)):
        vtype = type(value)
        if vtype is np.narray and value.shape[0] == 4 and value.shape[1] == 4:
            self.__body = value
        if vtype is v4.Quaternion:
            self = value.toMat4x4()
        else:
            tmat = position.toTraMat4x4()
            smat = scale.toScaMat4x4()
            rmat = rotation.toMat4x4()
            self.__body == smat.__body*rmat.__body*tmat.__body
    

