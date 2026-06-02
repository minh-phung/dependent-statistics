import numpy as np
import pandas as pd
import method
import noise

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
corr_stat = ["pear_corr", "dist_corr"]

'''
for each_stat in corr_stat:
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
# Compute y basis addition
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

y_val_subset_0 = ["poly", "perio_sin", "perio_cos", "exp"]
y_df_subset_0 = [y_poly, y_perio_sin, y_perio_cos, y_exp]

#-------------------------------------------

poly1 = y_poly[1].values
perio_sin1 = y_perio_sin[1].values
perio_cos1 = y_perio_cos[1].values
exp025 = y_exp[1].values

add_var = ["poly1", "perio_sin1", "perio_cos1", "exp025"]
add_val = [poly1, perio_sin1, perio_cos1, exp025]

#-------------------------------------------

y_df_subset_0_add =  np.full((len(y_val_subset_0), len(add_var)), None, dtype = object)

for i, each_y_0 in enumerate(y_df_subset_0):
	for j, each_add in enumerate(add_val):
		y_df_subset_0_add[i, j] = each_y_0.apply(lambda x: x + each_add)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Compute different statistics
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

corr_stat = ["pear_corr", "dist_corr"]

'''
for i, each_y_0_label in enumerate(y_val_subset_0):
	for j, each_add_label in enumerate(add_var):
		
		print("------------- " + each_y_0_label + " add " + each_add_label)
		
		y_val = y_df_subset_0_add[i,j]
		
		#-----------------------------------------
		
		for each_corr in corr_stat:
			print("----- " + each_corr)

			result = pd.DataFrame(index = [0], columns = y_val.columns)
			result.loc[0] = method.compute(x, y_val, stat = each_corr)
			
			result.to_csv(each_corr + "/y_" + each_y_0_label 
				      + "_add_" + each_add_label + ".csv",
				      index = False)
		
		#-----------------------------------------
		
		result = pd.DataFrame(index = mi_ksg_k, columns = y_val.columns)
		
		for j, each_k in enumerate(mi_ksg_k):
			print("----")
			print(each_k)
			result.loc[each_k] = method.compute(x, y_val, 
							    stat = 'mi_ksg', 
							    k_val = each_k)
		
		result.to_csv('mi_ksg' + "/y_" + each_y_0_label
			      + "_add_" + each_add_label + ".csv", 
			      index = False)
		
'''

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Plot
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
corr_stat = ["pear_corr", "dist_corr"]

add_var_color = ['blue', 'green', 'orange', 'yellow']

'''

for i, each_y_0 in enumerate(y_val_subset_0):
	print("------------------ " + each_y_0)
	
	for each_corr_stat in corr_stat:
		print(each_corr_stat)
		
		y_0_corr_df = pd.read_csv(each_corr_stat + "/y_" + 
					  each_y_0 + ".csv")
		
		y_0_corr_val = y_0_corr_df.values.flatten()

		x_0_corr_val = y_0_corr_df.columns.astype(float)
		# -------------------------------------

		plt.scatter(x_0_corr_val, y_0_corr_val,
			    color = 'red',
			    label = "y")

		# -------------------------------------

		for j, each_add_label in enumerate(add_var):
			
			y_0_add_corr_val = pd.read_csv(each_corr_stat + "/y_" +
					   each_y_0 + "_add_" + each_add_label +
					   ".csv").values.flatten()
			
			plt.scatter(x_0_corr_val, y_0_add_corr_val,
				    color = add_var_color[j],
				    label = "y + " + each_add_label,
				    s = 10)

		plt.legend()
		plt.title(each_y_0)
		plt.xlabel("parameter")
		plt.ylabel(each_corr_stat)
		
		if each_corr_stat == 'pear_corr':
			plt.ylim(-1, 1)
		else:
			plt.ylim(0,1)
					
		plt.savefig('plot/each_y_add_basis/' + each_y_0 
			    + "_" + each_corr_stat + ".png")
		plt.close()
		
'''
#-------------------------------------------
'''
mi_ksg_q = [0.95, 0.05]

for i, each_y_0 in enumerate(y_val_subset_0):
	print("------------------ " + each_y_0)
	
	y_0_mi_df = pd.read_csv("mi_ksg/y_" + each_y_0 + ".csv")
	
	x_0 = y_0_mi_df.columns.astype(float)

	# -------------------------------------
	
	y_0_mi_mean = np.mean(y_0_mi_df, axis = 0).values

	plt.scatter(x_0, y_0_mi_mean,
		    color = 'red',
		    label = "y")

	for j, each_add_label in enumerate(add_var):
		print(each_add_label)
		
		y_0_add_mi_df = pd.read_csv("mi_ksg/y_" + each_y_0 + "_add_" 
					    + each_add_label + ".csv")

		y_0_add_mi_mean = np.mean(y_0_add_mi_df, axis = 0).values
		
		plt.scatter(x_0, y_0_add_mi_mean,
			    color = add_var_color[j],
			    label = "y + " + each_add_label,
			    s = 10)

	plt.legend()
	plt.title(each_y_0)
	plt.xlabel("parameter")
	plt.ylabel("mi_ksg - mean")

	plt.savefig('plot/each_y_add_basis/' + each_y_0 
		    + "_mi_ksg_mean.png")
	plt.close()

	# -------------------------------------
	
	for each_q in mi_ksg_q:
		print("mi " + str(each_q))
		
		y_0_mi_q = np.quantile(y_0_mi_df, each_q, axis = 0)
		
		plt.scatter(x_0, y_0_mi_q,
			    color = 'red',
			    label = 'y')

		for j, each_add_label in enumerate(add_var):
			y_0_add_mi_df = pd.read_csv("mi_ksg/y_" + each_y_0 + "_add_" 
						    + each_add_label + ".csv")

			y_0_add_mi_q = np.quantile(y_0_add_mi_df, each_q, axis = 0)
			
			plt.scatter(x_0, y_0_add_mi_q,
				    color = add_var_color[j],
				    label = "y + " + each_add_label,
				    s = 10)
		
		plt.legend()
		plt.title(each_y_0)
		plt.xlabel("parameter")
		plt.ylabel("mi_ksg - " + str(each_q) + " quantile")
		
		plt.savefig('plot/each_y_add_basis/' + each_y_0 
			    + "_mi_ksg_" + str(each_q) + ".png")

		
		plt.close()


'''

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Compute homo- and heteroscedasticity
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

y_val_subset_0 = ["poly", "perio_sin", "perio_cos", "exp"]
y_df_subset_0 = [y_poly, y_perio_sin, y_perio_cos, y_exp]

#------------------------------------------------

add_noise_uni_std_frac = [0.5, 1]

y_df_subset_0_add_noise_uni =  np.full((len(y_val_subset_0), 
					len(add_noise_uni_std_frac)), 
					None, dtype = object)


for i, each_y_0 in enumerate(y_df_subset_0):
	for j, each_uni_std_frac in enumerate(add_noise_uni_std_frac):

		print("--------- " + str(each_uni_std_frac))
		
		y_df_subset_0_add_noise_uni[i,j] = each_y_0.apply(lambda x :
			noise.add(x, type = 'uni', std_frac = each_uni_std_frac)	
		)

#------------------------------------------------

add_noise_gaus_order = [0, 1, 2]
add_noise_gaus_std_frac = [0.5, 1]

