#coding:utf-8

import numpy as np
from . import wnpConst as wnp
from . import wnpVec3 as wv3
from . import wnpMatrix as mat


class Vector4:
    def __init__(self,w=0.,x=0.,y=0.,z=0.):
        self.__body = np.array([w,x,y,z])

    def __str__(self):
        return "[%f ,%f ,%f ,%f]"%(self.w,self.x,self.y,self.z)
    def __repr__(self):
        return "Vector4(%f ,%f ,%f ,%f)"%(self.w,self.x,self.y,self.z)

    @property
    def w(self):
        return self.__body[0]
    @w.setter
    def w(self,value):
        if type(value) in wnp.scalar_typeList:
            self.__body[0] = value

    @property
    def x(self):
        return self.__body[1]
    @x.setter
    def x(self,value):
        if type(value) in wnp.scalar_typeList:
            self.__body[1] = value

    @property
    def y(self):
        return self.__body[2]
    @y.setter
    def y(self,value):
        if type(value) in wnp.scalar_typeList:
            self.__body[2] = value

    @property
    def z(self):
        return self.__body[3]
    @z.setter
    def z(self,value):
        if type(value) in wnp.scalar_typeList:
            self.__body[3] = value

    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self,array):
        vtype = type(array)
        ar = array
        if vtype is list:
            ar = np.array(array)
        elif not vtype is np.array:
            raise TypeError("型が合いません listもしくはnumpy.arrayを使ってください")
        if ar.shape == (4,):
            self.__body = ar
        else:
            raise ValueError("サイズが合いません")
    
    
    def iadd_vec4(self,v):
        self.__body += v.body
    def add_vec4(self,v1,v2):
        self.__body = v1.body+v2.body
    def __add__(self,value):
        vtype = type(value)
        if vtype is Vector4:
            res == Vector4()
            res.add_vec4(self,value)
            return res
    def __iadd__(self,value):
        vtype = type(value)
        if vtype is Vector4:
            res == Vector4()
            res.add_vec4(self,value)
            return res


    def isub_vec4(self,v):
        self.__body -= v.body
    def sub_vec4(self,v1,v2):
        self.__body = v1.body-v2.body
    def __sub__(self,value):
        vtype = type(value)
        if vtype is Vector4:
            res == Vector4()
            res.sub_vec4(self,value)
            return res
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __isub__(self,value):
        vtype = type(value)
        if vtype is Vector4:
            res == Vector4()
            res.sub_vec4(self,value)
            return res
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))


    def idiv_scalar(self,scalar):
        self.__body /= scalar
    def div_scalar(self,vec4,scalar):
        self.__body = vec4.body / scalar
    def __truediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector4()
            res.div_scalar(self,value)
            return res
        raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __itruediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector4()
            res.div_scalar(self,value)
            return res
        raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))


    def imul_scalar(self,scalar):
        self.__body *= scalar
    def mul_scalar(self,vec4,scalar):
        self.__body = vec4.body * scalar
    def imul_vec4(self,vec):
        self.__body *= vec.body
    def mul_vec4(self,v1,v2):
        self.__body = v1.body * v2.body
    def mul_vec3(self,vec):
        array = self.__body * vec.body
        res = wv3.Vector3(array[0],array[1],array[2])
        return res
    def __mul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector4()
            res.mul_scalar(self,value)
            return res
        elif vtype is Vector4 or vtype is Quaternion:
            res = Vector4()
            res.mul_vec4(self,value)
            return res
        elif vtype is wv3.Vector3:
            res = self.mul_vec3(value)
            return res
        raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __imul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Vector4()
            res.mul_scalar(self,value)
            return res
        elif vtype is Vector4:
            res = Vector4()
            res.mul_vec4(self,value)
            return res
        elif vtype is Quaternion:
            pass
        raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    # 長さを求める
    def length(self):
        return np.linalg.norm(self.__body)

    # 正規化
    def normalize(self):
        return self / np.linalg.norm(self.__body)


class Quaternion(Vector4):
    def __init__(self,w=0.,x=0.,y=0.,z=0.):
        super(Quaternion,self).__init__(w,x,y,z)

    def __str__(self):
        return "[%f ,%f ,%f ,%f]"%(self.w,self.x,self.y,self.z)
    def __repr__(self):
        return "Quaternion(%f ,%f ,%f ,%f)"%(self.w,self.x,self.y,self.z)

    def set_axis_angle(self,angle,axis):
        print(np)
        sinhalfAngle = np.sin(angle/2.)
        self.x = axis.x * sinhalfAngle
        self.y = axis.y * sinhalfAngle
        self.z = axis.z * sinhalfAngle
        self.w = np.cos(angle/2.)

    def imul_qua(self,p):
        qx = self.x
        qy = self.y
        qz = self.z
        qw = self.w

        px = p.x
        py = p.y
        pz = p.z
        pw = p.w
        self.w = pw * qw - px * qx - py * qy - pz * qz
        self.x = pw * qx + px * qw + py * qz - pz * qy
        self.y = pw * qy - px * qz + py * qw + pz * qx
        self.z = pw * qz + px * qy - py * qx + pz * qw
    def mul_qua(self,q,p):
        qx = q.x
        qy = q.y
        qz = q.z
        qw = q.w

        px = p.x
        py = p.y
        pz = p.z
        pw = p.w
        self.w = pw * qw - px * qx - py * qy - pz * qz
        self.x = pw * qx + px * qw + py * qz - pz * qy
        self.y = pw * qy - px * qz + py * qw + pz * qx
        self.z = pw * qz + px * qy - py * qx + pz * qw
    def mul_vec3(self,v):
        conj = Quaternion()
        conj.body = np.array([self.w,-self.x,-self.y,-self.z],np.float64)
        vec = Quaternion()
        vec.body = np.array([0,v.x,v.y,v.z],np.float64)
        
        p = self*vec*conj
        res = wv3.Vector3(p.x,p.y,p.z)
        return res
    def __mul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Quaternion()
            res.mul_scalar(self,value)
            return res
        elif vtype is Vector4:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))
            res = Vector4()
            res.mul_vec4(self,value)
            return res
        elif vtype is Quaternion:
            res = Quaternion()
            res.mul_qua(self,value)
            return res
        elif vtype is wv3.Vector3:
            res = self.mul_vec3(value)
            return res
        elif vtype is wv3.Vector3:
            return mul_vec3(value)
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __imul__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            res = Quaternion()
            res.mul_scalar(self,value)
            return res
        elif vtype is Vector4:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))
            res = Vector4()
            res.mul_vec4(self,value)
            return res
        elif vtype is Quaternion:
            res = Quaternion()
            res.mul_qua(self,value)
            return res
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __truediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            inv = 1. / value
            res = Quaternion()
            res.mul_scalar(self,inv)
            return res
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def __itruediv__(self,value):
        vtype = type(value)
        if vtype in wnp.scalar_typeList:
            inv = 1. / value
            res = Quaternion()
            res.mul_scalar(self,inv)
            return res
        else:
            raise ValueError("右辺の型は%sとの演算ができません:%s"%(self,value))

    def toMat4x4(self):
        a = np.array([[self.x**2-self.y**2-self.z**2+self.w**2,(self.x*self.y-self.z*self.w)*2,(self.x*self.z+self.y*self.w)*2,0.],
                     [(self.x*self.y+self.z*self.w)*2,-self.x**2+self.y**2-self.z**2+self.w**2,(self.x*self.y-self.z*self.w)*2,0.],
                     [(self.x*self.y-self.z*self.w)*2,(self.x*self.y-self.z*self.w)*2,-self.x**2-self.y**2+self.z**2+self.w**2,0.],
                     [0.,0.,0.,1.]])
        return mat.Matrix4x4(a)
    
    def conjugate(self):
        """
        共役四元数を返す
        """
        res = self*-1.
        res.w*=-1.
        return res

    def inverse(self):
        """
        逆数を返す
        """
        res = self.conjugate()/self.length()**2
        return res

