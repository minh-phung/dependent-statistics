The goal of data modeling is to find the appropriate form for $$f(y|x)$$. In cases where the dimension of the predictor $$x$$ is much greater than the target $$y$$, models can either utilize all or a subset of the dimensions. As expected, the overhead for models that utilizes all will be higher than those that uses only a subset. The trade off is requiring feature selection.

There are many ways of selecting features. One is to find all subsets of all sizes of the predictor - a combinatory problem that might have large overhead, depending on the base model $$f$$. Assuming no intrinsic prior knowledge about the relationship $$f(y|x)$$, another approach is to use dependent statistics and develop a selection method based on them.

There exists many dependent statistics. A few includes: 
- Pearson Correlation Coefficient: used to determnine linear dependent, taking values $$[-1,1]$$, where 0 determines no dependent, with $$1$$ or $$-1$$ as perfect positive or negative linear correlation.
- Distance Correlation: used to determine dependent, taking values $$[0, 1]$$, where $$0$$ determines independent and $$1$$ for complete dependent.
- Mutual Information: used to determine dependent, where $$0$$ determines independent and $$>0$$ for dependent - depends on the type of random variable (discrete vs. continuous)
