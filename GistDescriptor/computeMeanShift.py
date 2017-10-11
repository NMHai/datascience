from sklearn.cluster import MeanShift;
import numpy as np; 
import time;
import pandas as pd; 

X = np.loadtxt('corpusFeatures1.csv', delimiter=',');

#Remove Nan Values in X
X = X[~np.isnan(X).any(axis=1)];

ms1 = MeanShift(bandwidth=0.2);
tic = time.time();
ms1.fit(X);
toc = time.time();
print "Elasped Time (s) = ", toc-tic;

labels1 = ms1.labels_;
labels1_u = np.unique(labels1);
l_sort_ind = np.argsort(labels1);

X_sort = np.zeros((X.shape[0],X.shape[1]));
for i in range(X.shape[0]):
  X_sort[i] = X[l_sort_ind[i]];

from scipy.spatial.distance import pdist,squareform

yd_sort = pdist(X_sort,'euclidean');
yd_sort_sq = squareform(yd_sort);
yd_sort_sq.shape;

import pylab as plt

plt.imshow(yd_sort_sq/yd_sort_sq.max());
plt.colorbar();
plt.show();
