import numpy as np

def add(x, type = '', **kwargs):
	
	noise_map = {
		'gaus' : gaus
	}
	
	func = noise_map.get(type)

	n = len(x)
	std = np.std(x)
	
	noise_val = func(n, std, **kwargs)
	
	return x + noise_val

def gaus(n, std = 1, std_frac = 1, order = 0):
	
	

	return np.random.normal(loc = 0, scale = std*std_frac, size = n)

