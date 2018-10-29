from pyrdmia import Rdmia

class RLS(object):
	
	def __init__(self):
		__model = 0.0
		__coefDetermination = 0.0
		__rmse = 0.0


	def fit(self,x,y):
		print (x)
		print (y)

		print ("X^T X ",x.T.dot(x))

		#x_1 = (inv_by_adjugate(midPointMatrix(x.T.dot(x))))
		x_1 = x.T.dot(x)
		x_1 = x_1.I
		print (x_1)

		#y_2 = midPointMatrix(x.T.dot(y))
		y_2 = x.T.dot(y)
		print (y_2)
		z = (x_1).dot(y_2)
		print (z)
		
		
		
		beta_0 = Rdmia.number(0)
		y_mean = Rdmia.number(0)
		x_mean = Rdmia.number(0)

		for val in y.data:
			y_mean+=val[0]
		for val in x.data:
			x_mean+=val[1]

		
		x_mean = x_mean/len(x.data)
		y_mean = y_mean/len(y.data)
		print ("MEDIA X: ",x_mean)
		print ("MEDIA Y: ",y_mean)

		beta_0 = Rdmia.array([[y_mean - (z.data[0][0]*(x_mean))]])
		print ("BETA_0 ",beta_0)

		print ("VALOR ORIGINAL",z)
		#print ("VALOR CORRIGIDO",z-beta_0)
		#beta = z-beta_0
		#print ("BETA_1 ",beta)
		x_square = Rdmia.zero()
		x_y = Rdmia.zero()
		
		for i in range(len(x.data)):
			x_y += x.data[i][0] * y.data[i][0]
			x_square+= x.data[i][0]**2

		print (x_y)
		print (x_square)
		print (x_y/x_square)


def billard(x):
	data = []
	l = Rdmia.number(0)
	u = Rdmia.number(0)
	for val in range(len(x.data)):
		l = 29.664 + 0.330*x.data[val][1].lower()
		u = 45.070 + 0.308*x.data[val][1].upper()
		data.append(Rdmia.number(l,u))
	return data

def coefDetermination(y,pred,y_mean):
	num = 0.0
	den = 0.0
	for val in range(len(y.data)):
		den+=qm.midpoint(((y.data[val][0]) - y_mean)**2)
		num+=qm.midpoint(((pred[val]) - y_mean)**2)
	return num/den

def RMSE(y_pred,y):
	lower = 0.0
	upper = 0.0
	for val in range(len(y.data)):
		lower+=(y.data[val][0].lower() - y_pred[val].lower())
		upper+=(y.data[val][0].upper() - y_pred[val].upper())
	
	lower = (lower**2.0/len(y.data))**(1.0/2.0)
	upper = (upper**2.0/len(y.data))**(1.0/2.0)
	return lower,upper

def var_array(r,r_mean):
	res_l = 0.0
	res_u = 0.0
	for val in range(len(r)):
		res_l+=((r[val][0].lower()) - r_mean.lower())**2.0
		res_u+=((r[val][0].upper()) - r_mean.upper())**2.0

	return res_l/len(r),res_u/len(r)

def var(r,r_mean):
	res_l = 0.0
	res_u = 0.0
	for val in range(len(r)):
		res_l+=((r[val].lower()) - r_mean.lower())**2.0
		res_u+=((r[val].upper()) - r_mean.upper())**2.0

	return res_l/len(r),res_u/len(r)

def cov(x,y):
	sum_xy_l = 0.0
	sum_xy_u = 0.0
	sum_x_l = 0.0
	sum_x_u = 0.0
	sum_y_l = 0.0
	sum_y_u = 0.0
	for val in range(len(x)):
		sum_xy_l+= x[val][0].lower()*y[val].lower()
		sum_xy_u+= x[val][0].upper()*y[val].upper()
		sum_x_l+= x[val][0].lower()
		sum_x_u += x[val][0].upper()
		sum_y_l += y[val].lower()
		sum_y_u = y[val].upper()
	
	return (sum_xy_l-(sum_x_l*sum_y_l)/len(x))/len(x),(sum_xy_u-(sum_x_u*sum_y_u)/len(x))/len(x)
	
if __name__=="__main__":

	Rdmia.setDotPrecision(2)

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

	regressor = RLS()
	regressor.fit(x,y)
	

	#x = Rdmia.array([[1,Rdmia.number(11,12)],[1,Rdmia.number(5)],[1,Rdmia.number(3)],[1,Rdmia.number(9)]])
	#y = Rdmia.array([[25],[13],[8],[20]])



	'''
	#FINAL
	billard_r = billard(x)
	print ("Value(INT) - PREDICT - Erro - R. Billard")
	r_list = []
	for val in range(len(x.data)):
		#print (z.data[0][0] + z.data[1][0]*x.data[val][1])
		if(type(z.data[0][0]) is Rdm):
			result = z.data[0][0] + z.data[1][0]*x.data[val][1]
			r_list.append(result)
			r = qm.midpoint(z.data[0][0] + z.data[1][0]*x.data[val][1])
			print (result,r,y.data[val]-r,billard_r[val])
		else:
			r = z.data[0][0] + z.data[1][0]*x.data[val][1]
			print (r,y.data[val][0]-r,billard_r[val])
		
	print("R^2 :",coefDetermination(y,r_list,y_mean))
	print("R^2 Billard:",coefDetermination(y,billard_r,y_mean))
	print("RMSE (lower,upper)",RMSE(r_list,y))
	print("RMSE_Billard (lower,upper)",RMSE(billard_r,y))
	cov_b_l,cov_b_u = cov(y.data,billard_r)
	aux_b_l,aux_b_u = (var(billard_r,y_mean))
	aux_2b_l,aux_2b_u = var_array(y.data,y_mean)
	print ("Covariancia BILLAR (lower,upper)",(cov_b_l/(aux_b_l*aux_2b_l)),(cov_b_u/(aux_b_u*aux_2b_u)))
	
	cov_b_l,cov_b_u = cov(y.data,r_list)
	aux_b_l,aux_b_u = (var(r_list,y_mean))
	aux_2b_l,aux_2b_u = var_array(y.data,y_mean)

	print ("Covariancia (lower,upper)",(cov_b_l/(aux_b_l*aux_2b_l)),(cov_b_u/(aux_b_u*aux_2b_u)))
	print ("Resultado Teste: ",z.data[0][0] + z.data[1][0]*Rdmia.number(118,126))
	'''
