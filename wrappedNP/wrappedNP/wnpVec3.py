#coding: utf-8

import numpy as np
from . import wnpConst as wnp
from . import wnpMatrix as mat


class Vector3:
    def __init__(self,x=0.,y=0.,z=0.):
        self.__body = np.array([x,y,z])

    def __str__(self):
        return "[%f ,%f ,%f]"%(self.x,self.y,self.z)
    def __repr__(self):
        return "vector3(%f ,%f ,%f)"%(self.x,self.y,self.z)

    @property
    def x(self):
        return self.__body[0]
    @x.setter
    def x(self,value):
        self.__body[0] = value

    @property
    def y(self):
        return self.__body[1]
    @y.setter
    def y(self,value):
        self.__body[1] = value

    @property
    def z(self):
        return self.__body[2]
    @z.setter
    def z(self,value):
        self.__body[2] = value
        
    @property
    def body(self):
        return self.__body
    
    def set_array_deep_copy(self,array):
        self.__body = array.copy()

    def set_array_shallow_copy(self,array):
        self.__body = array
        
    def set(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    #
    # 加算
    #
    def iadd_vec3(self,vec3):
        self.__body += vec3.body
    def add_vec3(self,vec3_1,vec3_2):
        self.__body = vec3_1.body + vec3_2.body
    def __add__(self,value):
        if type(value) is Vector3:
            res = Vector3()
            res.add_vec3(self,value)
            return res
    def __iadd__(self,value):
        if type(value) is Vector3:
            res = Vector3()
            res.add_vec3(self,value)
            return res
            


    #
    # 減算
    #
    def isub_vec3(self,vec3):
        self.__body -= vec3.body
    def sub_vec3(self,vec3_1,vec3_2):
        self.__body = vec3_1.body - vec3_2.body
    def __sub__(self,value):
        if type(value) is Vector3:
            res = Vector3()
            res.sub_vec3(self,value)
            return res
    def __isub__(self,value):
        if type(value) is Vector3:
            res = Vector3()
            res.sub_vec3(self,value)
            return res
            

    #
    # 除算
    #
    def idiv_scalar(self,scalar):
        self.__body /= scalar
    def div_scalar(self,vec3,scalar):
        self.__body = vec3.body / scalar
    def __truediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector3()
            res.div_scalar(self,value)
            return res
    def __itruediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector3()
            res.div_scalar(self,value)
            return res
            

    #
    # 乗算
    #
    def imul_scalar(self,scalar):
        self.__body *= scalar
    def mul_scalar(self,vec3,scalar):
        self.__body = vec3.body * scalar
    def __mul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector3()
            res.mul_scalar(self,value)
            return res
    def __imul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector3()
            res.mul_scalar(self,value)
            return res
            
    def toTraMat4x4(self):
        a = np.array([[1.,0.,0.,0.],
                     [0.,1.,0.,0.],
                     [0.,0.,1.,0.],
                     [self.x,self.y,self.z,1.]])
        return mat.Matrix4x4(a)
    def toScaMat4x4(self):
        a = np.array([[self.x,0.,0.,0.],
                     [0.,self.y,0.,0.],
                     [0.,0.,self.z,0.],
                     [0.,0.,0.,1.]])
        return  mat.Matrix4x4(a)

    # 長さを求める
    def length(self):
        return np.linalg.norm(self.__body)

    # 正規化
    def normalize(self):
        return self / np.linalg.norm(self.__body)
    
    # 内積
    def dot(self,vec3):
        if type(vec3) is Vector3:
            return np.dot(self.__body,vec3.body)

    # 外積
    def cross(self,vec3):
        if type(vec3) is Vector3:
            res = Vector3()
            res.set_array_shallow_copy(np.cross(self.__body,vec3.body))
            return res

