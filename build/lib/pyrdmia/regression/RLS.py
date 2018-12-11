from pyrdmia import Rdmia
from pyrdmia import Rdm
from pyrdmia.utils import QualitativeMetrics as qm

class RLS(object):
	
	def __init__(self):
		__model = 0.0
		__coefDetermination = 0.0
		__rmse = 0.0
		self._predictors = []


	def __str__(self):
		status = ''
		status = "R^2 :" + str(self._coefDetermination) + "\n"
		status += "RMSE :" + str(self._rmse) + "\n"
		return status

	def fit(self,x,y):
		#x_1 = (inv_by_adjugate(midPointMatrix(x.T.dot(x))))
		self._preProcessingData(x,y)

		#First part of method minimum square
		x_1 = x.T.dot(x)
		x_1 = x_1.I

		#y_2 = midPointMatrix(x.T.dot(y))
		y_2 = x.T.dot(y)


		#Calculated predictors beta
		z = (x_1).dot(y_2)
		self._predictors = Rdmia.array([z.data[i][0] for i in range(len(z.data))])

		#Calculte Status
		pred = self.predict(y)
		self._coefDetermination = self._coefDetermination(y,pred)
		self._rmse = self._RMSE(y,pred)
	
	def _preProcessingData(self,x,y):
		for i in range(len(y.data)):
			for k in range(len(x.data[0])):
				if(type(x.data[i][k]) is not Rdm):
					x.data[i][k] = Rdmia.number(x.data[i][k])
			if(type(y.data[i]) is not Rdm):
				y.data[i][0] = Rdmia.number(y.data[i][0])

	def predict(self,y):
		r_list = []
		for val in range(len(x.data)):
			if(type(self._predictors.data[0]) is Rdm):
				result = sum([self._predictors.data[i]*x.data[val][i] for i in range(len(self._predictors.data))])
				r_list.append(result)
				#r = qm.midpoint(self._predictors.data[0] + self._predictors.data[1]*x.data[val][1])
		return r_list
		
	def _mean(self,d):
		mean = Rdmia.number(0.0)
		for val in d.data:
			mean+=val[0]

		return mean/len(d.data)


	def _coefDetermination(self,y,pred):
		y_mean = self._mean(y)
		num = 0.0
		den = 0.0
		for val in range(len(y.data)):
			den+=qm.midpoint(((y.data[val][0]) - y_mean)**2)
			num+=qm.midpoint(((pred[val]) - y_mean)**2)
		return num/den
	
	def _RMSE(self,y,y_pred):
		lower = 0.0
		upper = 0.0
		for val in range(len(y.data)):
			lower+=(y.data[val][0].lower() - y_pred[val].lower())
			upper+=(y.data[val][0].upper() - y_pred[val].upper())
		
		lower = (lower**2.0/len(y.data))**(1.0/2.0)
		upper = (upper**2.0/len(y.data))**(1.0/2.0)
		return lower,upper




	
if __name__=="__main__":

	Rdmia.setDotPrecision(2)
	'''
	x = Rdmia.array([[Rdmia.number(1),Rdmia.number(90,100)],
	[Rdmia.number(1),Rdmia.number(90,130)],
	[Rdmia.number(1),Rdmia.number(140,180)],
	[Rdmia.number(1),Rdmia.number(110,142)],
	[Rdmia.number(1),Rdmia.number(90,100)],
	[Rdmia.number(1),Rdmia.number(130,160)],
	[Rdmia.number(1),Rdmia.number(60,100)],
	[Rdmia.number(1),Rdmia.number(130,160)],
	[Rdmia.number(1),Rdmia.number(110,190)],
	[Rdmia.number(1),Rdmia.number(138,180)],
	[Rdmia.number(1),Rdmia.number(110,150)]])

	y = Rdmia.array([[Rdmia.number(44,68)],
	[Rdmia.number(60,72)],
	[Rdmia.number(56,90)],
	[Rdmia.number(70,112)],
	[Rdmia.number(54,72)],
	[Rdmia.number(70,100)],
	[Rdmia.number(63,75)],
	[Rdmia.number(72,100)],
	[Rdmia.number(76,98)],
	[Rdmia.number(86,96)],
	[Rdmia.number(86,100)]
	])
	'''

	x = Rdmia.array([[1,Rdmia.number(11,12)],[1,Rdmia.number(5)],[1,Rdmia.number(3)],[1,Rdmia.number(9)]])
	y = Rdmia.array([[25],[13],[8],[20]])


	regressor = RLS()
	regressor.fit(x,y)
	ypred = regressor.predict(y)
	print (regressor)
	

