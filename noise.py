import numpy as np

def add(y, type = '', **kwargs):

	noise_map = {
		'gaus' : gaus,
		'uni'  : uni
	}
	
	func = noise_map.get(type)

	n = len(y)
	std = np.std(y)
	
	noise_val = func(n, std, **kwargs)

	return np.array(y + noise_val)

#--------------------------------------------------------------

def gaus(n, std, std_frac = 1, order = 0):
	
	if order == 0:
		scale_fac = np.ones(n)
	else:
		scale_fac = 1 + np.linspace(0, order, n)**order
	
	
	out = np.hstack([
		np.random.normal(loc = 0, scale = std* std_frac*i) for i in scale_fac
	])
	
	return out

#-------------------------------------------

def uni(n, std, std_frac = 1):
	
	abs_max = std * std_frac * np.sqrt(12) / 2

	return np.random.uniform(low = -abs_max, high = abs_max, size = n)