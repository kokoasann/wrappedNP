#coding: utf-8

import numpy as np
from .wnpVec3 import Vector3
from .wnpMatrix import Matrix4x4
from .wnpVec4 import Vector4,Quaternion

np.matrix4x4 = Matrix4x4
np.vector3 = Vector3
np.vector4 = Vector4;
np.quaternion = Quaternion;

if __name__ == "__main__":
    axis = wv3.Vector3(0.,1.,0.)

    rot = wv4.Quaternion()
    rot.set_axis_angle(np.pi*0.5,axis)
    axis.y = 0.
    axis.x = 1.
    res = rot * axis

    print(res.body)