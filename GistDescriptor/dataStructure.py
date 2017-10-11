import numpy as np;
import pandas as pd;

s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e']);
print s[:2];
print s;
s['a'] = 6;
print s;

print s.isnull();

print pd.Series(np.random.rand(5));

a = np.array([[1,2,3], [4,5,6], [7,8,np.nan]]);
print a; 

a = a[~np.isnan(a).any(axis=1)];
print a; 

 

