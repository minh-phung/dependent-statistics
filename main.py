import numpy as np
import pandas as pd
import method
from scipy.stats import norm
from sklearn.preprocessing import MinMaxScaler

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 6) 
plt.rcParams['figure.dpi'] = 500 


n = 1000
x = np.linspace(-1, 1, n)
mi_ksg_k = range(1, int(0.10*n))
np.random.seed(1)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Computing each y values: polynomial, periodic, exponential, gaussian, and 2 noise
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
# Noise: uniform, gaussian
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
# Computing different statistics
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
stat = ["pear_corr", "dist_corr"]

'''
for each_stat in stat:
	for i, each_y in enumerate(y_var):
		print(each_stat + "------------------------" + each_y)
	
		each_result = pd.DataFrame(index = [0], columns = y_df[i].columns)
		each_result.loc[0] = method.compute(x, y_df[i], stat = each_stat)
	
		each_result.to_csv(each_stat + "/y_" + each_y + ".csv", index = False)
'''
#-------------------------------------------
stat = "mi_ksg"

'''
for i, each_y in enumerate(y_var):
	print(stat + "------------------------" + each_y)
	
	each_result = pd.DataFrame(index = mi_ksg_k, columns = y_df[i].columns)
	
	for j, each_k in enumerate(mi_ksg_k):
		print("----")
		print(each_k)
		each_result.loc[each_k] = method.compute(x, y_df[i], 
							 stat = stat, 
							 k_val = each_k)
	each_result.to_csv(stat + "/y_" + each_y + ".csv", index = False)
'''

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Plot
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

y_val_subset_0 = ["poly", "sin", "cos", "exp"]
y_val_subset_1 = ["gaus", "noise_uni", "noise_gaus"]


mi_quantile = 0.95
scaler = MinMaxScaler()

for each_y_0 in y_val_subset_0:
	print(each_y + " ------------")
	
	# ------------------
	pear_corr_df = pd.read_csv("pear_corr/y_" + each_y_0 + ".csv")
	
	pear_corr_abs_val = np.abs(pear_corr_df.values).flatten()
	
	# ------------------
	dist_corr_df = pd.read_csv("dist_corr/y_" + each_y_0 + ".csv")
	
	dist_corr_val = dist_corr_df.values.flatten()

	# -------------------------------------
	x_val = pear_corr_df.columns.astype(float)
	
	plt.scatter(x_val, pear_corr_abs_val, 
		    color = "red", label = "abs(pear_corr)")
	
	plt.scatter(x_val, dist_corr_val,
		    color = "blue", label = "dist_corr")
	
	
	

	plt.title(each_y)
	plt.xlabel("parameter")
	plt.ylabel("score")

	plt.ylim(0, 1)
	plt.legend()

	plt.savefig("plot/" + each_y_0 + "_corr.png")
	plt.close()

	
	