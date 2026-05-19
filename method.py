import numpy as np
import pandas as pd
import infomeasure as im
import statsmodels.stats.dist_dependence_measures as s_s_d


def compute(x, dataf, stat = '', **kwargs):

	stat_map = {
		'mi_ksg': mi_ksg,
		'pear_corr': pearson_corr,
		'dist_corr': distance_corr
	}
	
	func = stat_map.get(stat)
	
	out = np.zeros(dataf.shape[1])

	for i, each_c in enumerate(dataf.columns):
		out[i] = func(x, dataf[each_c], **kwargs)
		
	return out

#-----------------------------------------------------

def pearson_corr(x, y):
	
	return np.corrcoef(x, y)[0,1]

#-----------------------------------------------------

def mi_ksg(x, y, k_val):
	
	return im.estimator(x, y, measure = 'mi', approach = 'ksg', 
			    k = k_val, noise_level = 0).result()

#-----------------------------------------------------

def distance_corr(x, y):	

	return s_s_d.distance_correlation(x, y)

