Dependent statistics are often used in feature selection, aiding the process of choosing a subsets of predictors, to both avoid overfitting and lower computational overhead. Taking the general form of the function being modeled to be $y(x) = f(x) + \epsilon$, they give a quantitative value of dependent between $y$ and $x$. There exists many dependent statistics. A few includes: 
- Pearson correlation coefficient: used to determine linear dependent, taking values $$[-1,1]$$, where 0 determines no linear dependent, with $$1$$ or $$-1$$ as perfect positive or negative linear correlation (numpy.corrcoef).
- Distance correlation: used to determine dependent, taking values $[0, 1]$, where $0$ determines independent and $1$ for complete dependent (statsmodels.stats.dist_dependence_measures.distance_correlation).
- Mutual information: used to determine dependent, taking values $[0,\infty)$, where $0$ determines independent and $>0$ for dependent (KSG - infomeasure).

Choosing which and how to use them becomes a question in itself - are there situations where one statistics is preferred over another? Given a vector space of function (closed under addition implies additive model), different statistics can be compared empirically on each elements of the basis.

Restricting the domain to $x \in [-1,1]$, four sets are chosen to be representative of the basis of four vector spaces of $f(x)$: 
- Polynomials: $`\{x^a\}`$ for $a=0,..., 100$
- Periodic: $`\{\sin(bx)\}` , `\{\cos(bx)\}`$ for $b=1,..., 50$
- Exponential: $`\{e^{cx}\}`$ for $c\in(0,5]$.

All three statistics listed above are computed, between $f(x)$ and $x$, for each elements in each set. Given that mutual information (in this case) is based on nearest-neighbour/have a hyperparameter, the chosen values are $k=1,..., 0.10 * n$, where $n = len(x)$, the number of $x$ points.

The results are plotted in 'plot/each_y'. Since the absolute value of Pearson correlation and distance correlation would have the same range value, they are compared within the same plots. Mutual information are plotted separately. As a point of comparison, the associated dependent statistics of
- Gaussian distribution $f(x) \sim N(0, 0.25)$
- Uniform noise $\epsilon \sim U(-1, 1)$
- Symmetric gaussian noise $\epsilon \sim N(0, 0.25)$
- Asymmetric gaussian noise $\epsilon \sim N(1, 0.25)$

are also plotted. For mutual information, the mean, 95th, and 5th percentile are plotted.

Furthermore, following the additive model assumption, each set of basis are added with an element from each of the four sets (for example, the polynomial set is added with each of $`\{x^1, \sin(x),\cos(x),e^{0.25 x}\}`$). Each dependent statistics are computed and plotted, in 'plot/each_y_add_basis'.

Finally, in looking at the effect of $\epsilon$ has on $y(x)$, as a function the standard deviation of the associated $f(x)$, two types of $\epsilon$ noise are added:
- Uniform: $\epsilon \sim U(p, q)$, where $p, q$ are the appropriate bound to set the standard deviation to be a $`\{0.5, 1\}`$ fraction of the standard deviation of $f(x)$.
- Gaussian: $\epsilon \sim N(0, l)$, where $l$ is set to be a $`\{0.5, 1\}`$ fraction of the standard deviation of $f(x)$, in cases where the standard deviation is constant, linearly increasing, and cubically increasing (homoscedasticity vs. heteroscedasticity comparison).

Each statistics are plotted, in 'plot/each_y_add_noise'.
