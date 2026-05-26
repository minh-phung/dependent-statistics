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

y_perio_sin = pd.DataFrame(data = sin_val, columns = wave_num)
y_perio_cos = pd.DataFrame(data = cos_val, columns = wave_num)

#-------------------------------------------
rate = np.linspace(5, 0, 20, endpoint = False)

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
y_noise_gaus_sym = pd.DataFrame(data = np.random.normal(loc = 0, scale = 0.25, size = n),
			    columns = [0])

#-------------------------------------------
y_noise_gaus_asym = pd.DataFrame(data = np.random.normal(loc = 1, scale = 0.25, size = n),
			    columns = [0])

#-----------------------------------------------------------------------------------
y_var = ["poly", "perio_sin", "perio_cos", "exp", "gaus",
	"noise_uni", "noise_gaus_sym", "noise_gaus_asym"]

y_df = [y_poly, y_perio_sin, y_perio_cos, y_exp, y_gaus,
	y_noise_uni, y_noise_gaus_sym, y_noise_gaus_asym]

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
# Plot: each y in subset 0 with each in subset 1
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

y_val_subset_0 = ["poly", "perio_sin", "perio_cos", "exp"]
y_val_subset_1 = ["gaus", "noise_uni", "noise_gaus_sym", "noise_gaus_asym"]

'''
for y_0 in y_val_subset_0:
	print("------------------ " + y_0)
	
	#---------------------
	y_0_pear_corr_df = pd.read_csv("pear_corr/y_" + y_0 + ".csv")
	y_0_pear_corr_abs_val = np.abs(y_0_pear_corr_df.values).flatten()	

	#---------------------
	y_0_dist_corr_df = pd.read_csv("dist_corr/y_" + y_0 + ".csv")
	y_0_dist_corr_val = y_0_dist_corr_df.values.flatten()

	#---------------------
	x_val = y_0_pear_corr_df.columns.astype(float)
	
	for y_1 in y_val_subset_1:
		print("-------- " + y_1)
		
		#---------------------
		y_1_pear_corr_df = pd.read_csv("pear_corr/y_" + y_1 + ".csv")
		y_1_pear_corr_abs_val = np.abs(y_1_pear_corr_df.values).item()
		
		#---------------------
		y_1_dist_corr_df = pd.read_csv("dist_corr/y_" + y_1 + ".csv")
		y_1_dist_corr_val = y_1_dist_corr_df.values.item()
		
		#---------------------
		plt.scatter(x_val, y_0_pear_corr_abs_val,
			    color = "blue", 
			    label = "abs(pear_corr)")
		plt.scatter(x_val, y_0_dist_corr_val,
			    color = "red", 
			    label = "dist_corr")
		
		plt.axhline(y_1_pear_corr_abs_val,
			    color = "blue", linestyle = '--', 
			    label = y_1 + " abs(pear_corr)")
		plt.axhline(y_1_dist_corr_val,
			    color = "red", linestyle = '--',
			    label = y_1 + " dist_corr")
		
		plt.title(y_0)
		plt.xlabel("parameter")
		plt.ylabel("correlation value")
		
		plt.legend()
		plt.ylim(0,1)
		plt.savefig("plot/each_y/" + y_0 + "_corr_" + y_1)
		
		plt.close()
'''		
#-------------------------------------------

'''
for y_0 in y_val_subset_0:
	print("------------------ " + y_0)
	
	y_0_mi_df = pd.read_csv("mi_ksg/y_" + y_0 + ".csv")
	
	y_0_mi_mean = np.mean(y_0_mi_df, axis = 0).values
	y_0_mi_q95 = np.quantile(y_0_mi_df, 0.95, axis = 0)
	y_0_mi_q5  = np.quantile(y_0_mi_df, 0.05, axis = 0)

	x_val = y_0_mi_df.columns.astype(float)
	
	
	for y_1 in y_val_subset_1:
		print("-------- " + y_1)
		y_1_mi = pd.read_csv("mi_ksg/y_" + y_1 + ".csv").values
		
		y_1_mi_mean = np.mean(y_1_mi)
		y_1_mi_q95 = np.quantile(y_1_mi, 0.95)
		y_1_mi_q5  = np.quantile(y_1_mi, 0.05)
		
		#-------------------------------

		plt.errorbar(
			x_val, y_0_mi_mean,
			yerr = [y_0_mi_mean - y_0_mi_q5,
				y_0_mi_q95 - y_0_mi_mean],
			label = "mean (95th - 5th)",
			color = "red"
		)

		plt.axhline(y_1_mi_mean,
			    color = "blue", linestyle = '--',
			    label = y_1 + " mean (95th - 5th)")
		plt.axhline(y_1_mi_q95,
			    color = "blue", linestyle = '--')
		plt.axhline(y_1_mi_q5,
			    color = "blue", linestyle = '--')
	
		
		plt.title(y_0)
		plt.xlabel("parameter")
		plt.ylabel("mi_ksg score")

		plt.legend()
		plt.savefig("plot/each_y/" + y_0 + "_mi_" + y_1)
		plt.close()
'''

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Compute 
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


y_val_subset_0 = ["poly", "perio_sin", "perio_cos", "exp"]

y_df_subset_0 = [y_poly, y_perio_sin, y_perio_cos, y_exp]

#-------------------------------------------

poly1 = y_poly[1].values
perio_sin1 = y_perio_sin1[1].values
perio_cos1 = y_perio_cos1[1].values
exp1 = y_exp[1].values
