#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @author: nmhai

import pandas as pd, numpy as np;
from  sklearn import linear_model;
from sklearn.cross_validation import train_test_split;

# data = pd.read_csv('all-stocks-cleaned.csv');
data = pd.read_csv("all-stocks-cleaned.csv");
print data;
# Insert missing values
data = data.fillna(method='ffill');
print data;
stock = np.array(data);
# remove Nan values
# stock = stock[~np.isnan(stock).any(axis=1)];

openingPrice = stock[:, 1]
closingPrice = stock[:, 5]

print((np.min(openingPrice)))
print((np.min(closingPrice)))
print((np.max(openingPrice)))
print((np.max(closingPrice)))

openingPriceTrain, openingPriceTest, closingPriceTrain, closingPriceTest = \
    train_test_split(openingPrice, closingPrice, test_size=0.25, random_state=42)


openingPriceTrain = np.reshape(openingPriceTrain,(openingPriceTrain.size,1))
openingPriceTrain = openingPriceTrain.astype(np.float64, copy=False)
# openingPriceTrain = np.arange(openingPriceTrain, dtype=np.float64)

closingPriceTrain = np.reshape(closingPriceTrain,(closingPriceTrain.size,1))
closingPriceTrain = closingPriceTrain.astype(np.float64, copy=False)

openingPriceTest = np.reshape(openingPriceTest,(openingPriceTest.size,1))
closingPriceTest = np.reshape(closingPriceTest,(closingPriceTest.size,1))

regression = linear_model.LinearRegression()

regression.fit(openingPriceTrain, closingPriceTrain)

predicted = regression.predict(openingPriceTest)

print predicted;