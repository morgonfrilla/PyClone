'''
  File name           : main.py
  Author              : Fredrik Dahlin
  Date created        : 11/1/2016
  Date last modified  : 11/1/2016
  Python Version      : 3.4
'''
import priors
import utility
import pyclone_binomial



# Load data
data, sample_ids = utility.loadDataPyClone()

tumour_content = {}
for id in sample_ids:
  tumour_content[id] = 1.0


trace_dir = 'trace'

num_iters = 10000

alpha = 1

alpha_priors = {
	'shape': 1.0,
	'rate': 0.001
}

pyclone_binomial.run_pyclone_binomial_analysis(data, sample_ids, tumour_content, trace_dir, num_iters, alpha, alpha_priors)

