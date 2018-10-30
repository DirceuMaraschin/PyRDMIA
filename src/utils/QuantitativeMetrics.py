from pyrdmia.core import Rdmia as rdmia
from pyrdmia.core import Rdm
import numpy as np

# Covariance
# Media


'''


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


'''
