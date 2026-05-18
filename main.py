import numpy as np
import pandas as pd
import infomeasure as im
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 500


n = 1000

x = np.linspace(-1, 1, n)
poly_order = range(1, 100)

poly_val = np.column_stack([x**k for k in poly_order])
y_poly = pd.DataFrame(
    data=poly_val, columns=poly_order
)


k_range = range(1, int(0.10*n))

'''
mi_poly = pd.DataFrame(index = k_range, columns = poly_order)

for each_order in poly_order:
	print("order " + str(each_order))
	for each_k in k_range:

        	mi_poly.loc[each_k, each_order] = im.estimator(x, y_poly[each_order],
                	                                       measure = 'mi',
                        	                               approach = 'ksg',
                                	                       k = each_k,
                                        	               noise_level = 0).result()

mi_poly.to_csv("mi/poly.csv", index = False)
'''

mi_poly = pd.read_csv("mi/poly.csv")
mi_poly.columns = mi_poly.columns.astype(int)


mi_mean = np.zeros(len(poly_order))
mi_lower = np.zeros(len(poly_order))
mi_upper = np.zeros(len(poly_order))

mi_max = np.zeros(len(poly_order))

k_100_percentile = np.zeros(len(poly_order))
k_95_percentile = np.zeros(len(poly_order))
k_75_percentile = np.zeros(len(poly_order))


'''
for i, each_order in enumerate(poly_order):
		
	y = mi_poly[each_order]
	
	mi_mean[i] = np.mean(y)
	mi_lower[i] = mi_mean[i] - np.quantile(y, 0.05)
	mi_upper[i] = np.quantile(y, 0.95) - mi_mean[i]

	# ---------------------------
	mi_max[i] = np.max(y)
	k_100_percentile[i] = mi_poly[each_order].idxmax()
	
	q_95 = np.quantile(y, 0.95)
	idx_95 = ((y-q_95)**2).idxmin()
	k_95_percentile[i] = idx_95
	
	q_75 = np.quantile(y, 0.75)
	idx_75 = ((y-q_75)**2).idxmin()
	k_75_percentile[i] = idx_75
	
	# ---------------------------
	#plt.scatter(y.index, y.values)
	#plt.xlabel("K-val")
	#plt.ylabel("MI score")
	#plt.savefig("mi/poly/hist/" + str(each_order) + ".png")
	#plt.close()
	
	
plt.errorbar(
	x = poly_order,
    	y = mi_mean,
    	yerr = [mi_lower, mi_upper],
    	elinewidth = 0.5,
)

plt.xlabel("Polynomial order")
plt.ylabel("MI score (KSG)")
plt.savefig("mi/poly/mean.png")
plt.close()

plt.scatter(poly_order, k_100_percentile)
plt.xlabel("Polynomial order")
plt.ylabel("100th percentile KSG - associated k value")
plt.savefig("mi/poly/100th_k.png")
plt.close()

plt.scatter(poly_order, k_95_percentile)
plt.xlabel("Polynomial order")
plt.ylabel("95th percentile KSG - associated k value")
plt.savefig("mi/poly/95th_k.png")
plt.close()

plt.scatter(poly_order, k_75_percentile)
plt.xlabel("Polynomial order")
plt.ylabel("75th percentile KSG - associated k value")
plt.savefig("mi/poly/75th_k.png")
plt.close()

'''

y_poly_add_1  = pd.DataFrame(np.zeros(y_poly.shape),
			     columns = poly_order)
y_poly_add_2  = pd.DataFrame(np.zeros(y_poly.shape),
			     columns = poly_order)
y_poly_add_n1 = pd.DataFrame(np.zeros(y_poly.shape),
			     columns = poly_order)


for each_order in poly_order:
	#print("--" + str(each_order))
	
	y_poly_add_1[each_order] = y_poly[each_order] + y_poly[1]
	y_poly_add_2[each_order] = y_poly[each_order] + y_poly[2]

	if each_order == 1:
		y_poly_add_n1[each_order] = y_poly[each_order]
	else:
		y_poly_add_n1[each_order] = y_poly[each_order] + y_poly[each_order-1]



'''

mi_poly_add_1  = pd.DataFrame(index = k_range, columns = poly_order)
mi_poly_add_2  = pd.DataFrame(index = k_range, columns = poly_order)
mi_poly_add_n1 = pd.DataFrame(index = k_range, columns = poly_order)


for each_order in poly_order:
	print("order " + str(each_order))
	for each_k in k_range:
		mi_poly_add_1.loc[each_k, each_order] = im.estimator(x, y_poly_add_1[each_order],
                	                                             measure = 'mi',
                        	                              	     approach = 'ksg',
                                	                             k = each_k,
                                        	                     noise_level = 0).result()
		
		mi_poly_add_2.loc[each_k, each_order] = im.estimator(x, y_poly_add_2[each_order],
                	                                             measure = 'mi',
                        	                              	     approach = 'ksg',
                                	                             k = each_k,
                                        	                     noise_level = 0).result()
		
		mi_poly_add_n1.loc[each_k, each_order] = im.estimator(x, y_poly_add_n1[each_order],
                	                                              measure = 'mi',
                        	                              	      approach = 'ksg',
                                	                              k = each_k,
                                        	                      noise_level = 0).result()
		

mi_poly_add_1.to_csv("mi/poly_add_1.csv", index = False)
mi_poly_add_2.to_csv("mi/poly_add_2.csv", index = False)
mi_poly_add_n1.to_csv("mi/poly_add_n1.csv", index = False)

'''

mi_poly_add_1 = pd.read_csv("mi/poly_add_1.csv")
mi_poly_add_1.columns = mi_poly_add_1.columns.astype(int)

mi_poly_add_2 = pd.read_csv("mi/poly_add_2.csv")
mi_poly_add_2.columns = mi_poly_add_2.columns.astype(int)

mi_poly_add_n1 = pd.read_csv("mi/poly_add_n1.csv")
mi_poly_add_n1.columns = mi_poly_add_n1.columns.astype(int)



add_1_comparison = pd.DataFrame(index = range(4), columns = poly_order)
add_2_comparison = pd.DataFrame(index = range(4), columns = poly_order)
add_n1_comparison = pd.DataFrame(index = range(4), columns = poly_order)


quantile_list = [1, .95, .75]


for each_order in poly_order:

	y = mi_poly[each_order]
	y_1 = mi_poly[1]
	y_2 = mi_poly[2]
	
	if each_order == 1:
		y_n1 = mi_poly[1]
	else:
		y_n1 = mi_poly[each_order - 1]
	

	y_add_1 = mi_poly_add_1[each_order]
	y_add_2 = mi_poly_add_2[each_order]
	y_add_n1 = mi_poly_add_n1[each_order]

	for i, each_q in enumerate(quantile_list):
		val_1 = (np.quantile(y_add_1, each_q) - np.quantile(y, each_q)) / np.quantile(y_1, each_q)
		add_1_comparison.loc[i, each_order] = val_1
		
		val_2 = (np.quantile(y_add_2, each_q) - np.quantile(y, each_q)) / np.quantile(y_2, each_q)
		add_2_comparison.loc[i, each_order] = val_2
		
		val_n1 = (np.quantile(y_add_n1, each_q) - np.quantile(y, each_q)) / np.quantile(y_n1, each_q)
		add_n1_comparison.loc[i, each_order] = val_n1
		

	add_1_comparison.loc[3, each_order] = (np.mean(y_add_1) - np.mean(y)) / np.mean(y_1)
	add_2_comparison.loc[3, each_order] = (np.mean(y_add_2) - np.mean(y)) / np.mean(y_2)
	add_n1_comparison.loc[3, each_order] = (np.mean(y_add_n1) - np.mean(y)) / np.mean(y_n1)



var_list = ["100th", "95th", "75th", "mean"]

print(add_1_comparison)


for i, each_var in enumerate(var_list):
	
	plt.scatter(poly_order, add_1_comparison.loc[i])
	plt.xlabel("Polynomial order")
	plt.ylabel("Change in " + each_var + " (percentage of poly order 1)")
	plt.savefig("mi/poly_add_1/" + each_var + ".png")
	plt.close()

	plt.scatter(poly_order, add_2_comparison.loc[i])
	plt.xlabel("Polynomial order")
	plt.ylabel("Change in " + each_var + " (percentage of poly order 2)")
	plt.savefig("mi/poly_add_2/" + each_var + ".png")
	plt.close()

	plt.scatter(poly_order, add_n1_comparison.loc[i])
	plt.xlabel("Polynomial order")
	plt.ylabel("Change in " + each_var + " (percentage of poly order n-1)")
	plt.savefig("mi/poly_add_n1/" + each_var + ".png")
	plt.close()

	

