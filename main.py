import numpy as np
import pandas as pd
import method
from scipy.stats import norm


n = 1000
x = np.linspace(-1, 1, n)
mi_ksg_k = range(1, int(0.10*n))
np.random.seed(1)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

poly_order = range(1, 100)

poly_val = np.column_stack([x**k for k in poly_order])

y_poly = pd.DataFrame(data=poly_val, columns=poly_order)

#-------------------------------------------
wave_num = range(1, 50)

sin_val = np.column_stack([np.sin(k*x) for k in wave_num])
cos_val = np.column_stack([np.cos(k*x) for k in wave_num])

y_sin = pd.DataFrame(data = sin_val, columns = wave_num)
y_cos = pd.DataFrame(data = cos_val, columns = wave_num)

#-------------------------------------------
rate = np.linspace(-5, 5, 10)

exp_val = np.column_stack([np.exp(k*x) for k in rate])

y_exp = pd.DataFrame(data = exp_val, columns = rate)

#-------------------------------------------
y_gaus = pd.DataFrame(data = norm.pdf(x, loc = 0, scale = 0.25),
	   	      columns = [0])

#-------------------------------------------
#------------------------------------------- 
y_noise_uni = pd.DataFrame(data = np.random.uniform(low = -1, high = 1, size = n),
			   columns = [0])

#-------------------------------------------
y_noise_gaus = pd.DataFrame(data = np.random.normal(loc = 0, scale = 0.25, size = n),
			    columns = [0])

#-----------------------------------------------------------------------------------
y_var = ["poly", "sin", "cos", "exp", "gaus",
	"noise_uni", "noise_gaus"]

y_df = [y_poly, y_sin, y_cos, y_exp, y_gaus,
	y_noise_uni, y_noise_gaus]

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
var = "pear_corr"

'''
for i, each_y in enumerate(y_var):
	print(var + "------------------------" + each_y)
	
	each_result = pd.DataFrame(index = [0], columns = y_df[i].columns)
	each_result.loc[0] = method.compute(x, y_df[i], stat = var)
	
	each_result.to_csv(var + "/y_" + each_y + ".csv", index = False)
'''
#-------------------------------------------
var = "mi_ksg"

'''
for i, each_y in enumerate(y_var):
	print(var + "------------------------" + each_y)
	
	each_result = pd.DataFrame(index = mi_ksg_k, columns = y_df[i].columns)
	
	for j, each_k in enumerate(mi_ksg_k):
		print("----")
		print(each_k)
		each_result.loc[each_k] = method.compute(x, y_df[i], 
							 stat = var, 
							 k_val = each_k)
	each_result.to_csv(var + "/y_" + each_y + ".csv", index = False)
'''
#-------------------------------------------
var = "dist_corr"

'''
for i, each_y in enumerate(y_var):
	print(var + "------------------------" + each_y)
	
	each_result = pd.DataFrame(index = [0], columns = y_df[i].columns)
	each_result.loc[0] = method.compute(x, y_df[i], stat = var)
	
	each_result.to_csv(var + "/y_" + each_y + ".csv", index = False)
'''
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

var_list = ["pear_corr", "mi_ksg", "dist_corr"]



