# PyRDMIA Python Library 2018
# RDM-IA implementation by
# Dirceu Maraschin Jr
# Lucas Tortelli

'''
This file is responsible for creating RDM numbers and setting the 
precision of operation in calculations using PyRDMIA.
'''
from __future__ import print_function
from .Rdm import *
import itertools, copy

class Rdmia(object):

    # Default precision
    _precision = 0.01

    @staticmethod
    def precision():
        return Rdmia._precision

    @staticmethod
    def setDotPrecision(val):
       Rdmia._precision = val#10**(-val)

    @staticmethod
    def one():
        return Rdm(1.0,None,Rdmia._precision)
    
    @staticmethod
    def zero():
        return Rdm(0.0,None,Rdmia._precision)

    @staticmethod
    def number(x,y=None):
        if y is None:
            return Rdm(x,None,Rdmia._precision)
        else:
            return Rdm(x,y,Rdmia._precision)

    @staticmethod
    def isiterable(data):
        try:
            chkit = iter(data)
        except TypeError:
            return False
        return True

    @staticmethod
    def array(data):
        arr = SimpleArray()
        arr.shape = []
        if not Rdmia.isiterable(data):
            raise ValueError("Input must be iterable")
        arr._ValidateShape(data, 0)
        arr.data = data
        arr.shape = tuple(arr.shape)
        return arr

    @staticmethod
    def midPointMatrix(data):
        for i in range(data.shape[0]):
            for k in range(data.shape[1]):
                if(type(data.data[i][k]) is Rdm):
                    data.data[i][k] = rdmia.number(qm.midpoint(data.data[i][k]))
                
        return data

    @staticmethod
    def zeros(shape):
        arr = SimpleArray()
        arr.shape = tuple(shape)
        if not Rdmia.isiterable(shape):
            raise ValueError("Shape must be iterable")
        arr.data = []
        def GenData(shape, leafs):
            dim = shape.pop(0)
            newLeafs = []
            if len(shape) == 0:
                for l in leafs:
                    for i in range(dim):
                        l.append(0.0)
            else:
                for l in leafs:
                    for i in range(dim):
                        nl = []
                        l.append(nl)
                        newLeafs.append(nl)
                GenData(shape, newLeafs)
                
        GenData(list(arr.shape)[:], [arr.data])
        return arr

    @staticmethod
    def identity(dim):
        mat = Rdmia.zeros((dim, dim))
        for i in range(dim):
            mat.data[i][i] = 1.0
        return mat


class SimpleArray(object):
	def __init__(self):
		self.shape = []
		self.data = None

	
	def _ValidateShape(self, data, ind):
		if not Rdmia.isiterable(data):
			return

		if ind >= len(self.shape):
			self.shape.append(len(data))
		else:
			if self.shape[ind] != len(data):
				raise ValueError("Inconsistent shape")
		
		for val in data:
			self._ValidateShape(val, ind+1)

	def __repr__(self):
		return (self.__class__.__name__+"("+self.data+")")


	def __str__(self):
		#print (self.data)
		matrix = ''
		for row in self.data:
			matrix += str(row)+"\n"
		return matrix

	def dot(self, rhs):
		#This also standard matrix multiplication
		if not isinstance(rhs, self.__class__) and Rdmia.isiterable(rhs):		
			rhs = Rdmia.array(rhs)
		if len(self.shape) != 2 or len(rhs.shape) != 2:
			raise NotImplementedError("Only implemented for 2D matricies")
		if self.shape[1] != rhs.shape[0]:
			raise ValueError("Matrix size mismatch")
		m = self.shape[1]
		result = Rdmia.zeros((self.shape[0], rhs.shape[1]))
		for i in range(result.shape[0]):
			for j in range(result.shape[1]):
				tot = 0.0
				for k in range(m):
					aik = self.data[i][k]
					bkj = rhs.data[k][j]
					tot += aik * bkj
				result.data[i][j] = tot

		return result

	def __add__(self, rhs):
		if not isinstance(rhs, self.__class__) and Rdmia.isiterable(rhs):		
			rhs = Rdmia.array(rhs)
		if self.shape != rhs.shape:
			raise ValueError("Matrix size mismatch")
		result = Rdmia.zeros(self.shape)
		def AddFunc(ind, a, b, out):
			if ind == len(self.shape):
				raise ValueError("Invalid matrix")
			if ind == len(self.shape) - 1:
				for i, (av, bv) in enumerate(zip(a, b)):
					out[i] = av + bv
			else:
				ind += 1
				for ar, br, outr in zip(a, b, out):
					AddFunc(ind, ar, br, outr)		

		AddFunc(0, self.data, rhs.data, result.data)
		return result

	def __mul__(self, rhs):
		if not isinstance(rhs, self.__class__) and Rdmia.isiterable(rhs):		
			rhs = Rdmia.array(rhs)

		if isinstance(rhs, self.__class__):
			#Do element-wise matrix multiplication

			if self.shape != rhs.shape:
				raise ValueError("Matrix size mismatch")
			result = Rdmia.zeros(self.shape)
			def MultFunc(ind, a, b, out):
				if ind == len(self.shape):
					raise ValueError("Invalid matrix")
				if ind == len(self.shape) - 1:
					for i, (av, bv) in enumerate(zip(a, b)):
						out[i] = av * bv
				else:
					ind += 1
					for ar, br, outr in zip(a, b, out):
						MultFunc(ind, ar, br, outr)		

			MultFunc(0, self.data, rhs.data, result.data)
			return result
		else:
			#Do scalar multiplication to entire matrix (element-wise)
			result = Rdmia.zeros(self.shape)
			def MultFunc2(ind, a, b, out):
				if ind == len(self.shape):
					raise ValueError("Invalid matrix")
				if ind == len(self.shape) - 1:
					for i, av in enumerate(a):
						out[i] = av * b
				else:
					ind += 1
					for ar, outr in zip(a, out):
						MultFunc2(ind, ar, b, outr)		

			MultFunc2(0, self.data, rhs, result.data)
			return result

	def __sub__(self, rhs):
		if not isinstance(rhs, self.__class__) and Rdmia.isiterable(rhs):		
			rhs = Rdmia.array(rhs)
		if self.shape != rhs.shape:
			raise ValueError("Matrix size mismatch")
		negRhs = rhs * -1
		return self + negRhs

	def conj(self):
		result = Rdmia.zeros(self.shape)
		def AddFunc(ind, a, out):
			if ind == len(self.shape):
				raise ValueError("Invalid matrix")
			if ind == len(self.shape) - 1:
				for i, av in enumerate(a):
					if isinstance(av, complex):
						out[i] = av.conjugate()
					else:
						out[i] = av
			else:
				ind += 1
				for ar, outr in zip(a, out):
					AddFunc(ind, ar, outr)		

		AddFunc(0, self.data, result.data)
		return result

	@property
	def T(self):
		if len(self.shape) <= 1:
			return self
		if len(self.shape) != 2:
			raise NotImplementedError("Only implemented for 1D and 2D matricies")	
		result = Rdmia.zeros((self.shape[1], self.shape[0]))
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				result.data[j][i] = self.data[i][j]
		return result

	def copy(self):
		return Rdmia.array(copy.deepcopy(self.data))

def perm_parity(lst):
	'''\
	Given a permutation of the digits 0..N in order as a list, 
	returns its parity (or sign): +1 for even parity; -1 for odd.
	From https://code.activestate.com/recipes/578227-generate-the-parity-or-sign-of-a-permutation/
	'''
	parity = 1
	for i in range(0,len(lst)-1):
		if lst[i] != i:
			parity *= -1
			mn = min(range(i,len(lst)), key=lst.__getitem__)
			lst[i],lst[mn] = lst[mn],lst[i]
	return parity	

def det(mat):
	if not isinstance(mat, SimpleArray) and Rdmia.isiterable(mat):		
		mat = Rdmia.array(mat)
	if len(mat.shape) != 2:
		raise NotImplementedError("Only implemented for 2D matricies")
	if mat.shape[0] != mat.shape[1]:
		raise ValueError("Matrix must be square")
	n = mat.shape[0]
	
	#Leibniz formula for the determinant
	total2 = 0.0
	for perm in itertools.permutations(range(n)):
		total1 = 1.0
		for i, j in zip(range(n), perm):
			total1 *= mat.data[i][j]
		total2 += perm_parity(list(perm)) * total1
	return total2

def delete(mat, ind, axis=0):
	if not isinstance(mat, SimpleArray) and Rdmia.isiterable(mat):		
		mat = Rdmia.array(mat)
	newShape = list(mat.shape)[:]
	newShape[axis] -= len(ind)
	result = Rdmia.zeros(newShape)
	def CopyWithDelete(currentAxis, ind, axis, matdata, resultData):
		if currentAxis < len(mat.shape)-1:
			count = 0
			for i, data in enumerate(matdata):
				if currentAxis == axis and i in ind:
					continue
				CopyWithDelete(currentAxis + 1, ind, axis, data, resultData[count])
				count += 1
		else:
			count = 0
			for i, val in enumerate(matdata):
				if currentAxis == axis and i in ind:
					continue
				resultData[count] = val
				count += 1

	CopyWithDelete(0, ind, axis, mat.data, result.data)
	return result

def adjugate(mat):
	if not isinstance(mat, SimpleArray) and Rdmia.isiterable(mat):		
		mat = Rdmia.array(mat)
	#Find the adjugate matrix
	if len(mat.shape) != 2:
		raise NotImplementedError("Only implemented for 2D matricies")
	result = Rdmia.zeros(mat.shape)
	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):
			submat = delete(mat, [j], 0)
			submat2 = delete(submat, [i], 1)
			result.data[i][j] = ((-1)**(i+j))*det(submat2)
	return result

def inv_by_adjugate(mat, eps=1e-8):
	#Find inverse based on find the adjugate matrix
	#which is inefficient for large matrices.
	if not isinstance(mat, SimpleArray) and Rdmia.isiterable(mat):		
		mat = Rdmia.array(mat)
	if len(mat.shape) != 2:
		raise NotImplementedError("Only implemented for 2D matricies")
	if mat.shape[0] != mat.shape[1]:
		raise ValueError("Matrix must be square")
	mdet = det(mat)
	if (type(mdet) is Rdm):
		mdet = qm.midpoint(mdet)
	if abs(mdet) < eps:
		raise RuntimeError("Matrix is not invertible (its determinant is zero)")
	return adjugate(mat) * (1.0 / float(mdet))

def inv_by_gauss_jordan(mat, eps=1e-8):
	#Find inverse based on gauss-jordan elimination.

	if not isinstance(mat, SimpleArray) and Rdmia.isiterable(mat):		
		mat = Rdmia.array(mat)
	if len(mat.shape) != 2:
		raise NotImplementedError("Only implemented for 2D matricies")
	if mat.shape[0] != mat.shape[1]:
		raise ValueError("Matrix must be square")
	mdet = det(mat)

	if(type(mdet) is Rdm):
		mdet = qm.midpoint(mdet)
	if abs(mdet) < eps:
		raise RuntimeError("Matrix is not invertible (its determinant is zero)")

	#Create aux matrix
	n = mat.shape[0]
	auxmat = Rdmia.identity(n)

	#Convert to echelon (triangular) form
	mat = copy.deepcopy(mat)
	for i in range(n):
		#Find highest value in this column
		maxv = 0.0
		maxind = None
		for r in range(i, n):
			v = mat.data[r][i]
			if(type(v) is Rdm):
				v = abs(qm.midpoint(v))
			if maxind is None or abs(v) > maxv:
				if(type(v) is Rdm):
					maxv = abs(qm.midpoint(v))
				else:
					maxv = abs(v)
				maxind = r
		
		if maxind != i:
			#Swap this to the current row, for numerical stability
			mat.data[i], mat.data[maxind] = mat.data[maxind], mat.data[i]
			auxmat.data[i], auxmat.data[maxind] = auxmat.data[maxind], auxmat.data[i]

		activeRow = mat.data[i]
		activeAuxRow = auxmat.data[i]
		for r in range(i+1, n):
			scale = mat.data[r][i] / mat.data[i][i]
			cursorRow = mat.data[r]
			cursorAuxRow = auxmat.data[r]
			for c in range(n):
				cursorRow[c] -= scale * activeRow[c]
				cursorAuxRow[c] -= scale * activeAuxRow[c]

	#Finish elimination
	for i in range(n-1, -1, -1):
		activeRow = mat.data[i]
		activeAuxRow = auxmat.data[i]
		for r in range(i, -1, -1):
			cursorRow = mat.data[r]
			cursorAuxRow = auxmat.data[r]
			if r == i:
				scaling = activeRow[i]
				for c in range(n):
					print(cursorRow[c],scaling)
					cursorRow[c] /= scaling
					cursorAuxRow[c] /= scaling
			else:
				scaling = cursorRow[i]
				for c in range(n):
					cursorRow[c] -= activeRow[c] * scaling
					cursorAuxRow[c] -= activeAuxRow[c] * scaling
			
	return auxmat