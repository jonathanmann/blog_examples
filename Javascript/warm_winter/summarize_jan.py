#!/usr/bin/env python
import pandas as pd
w = pd.read_csv('nyc_early_jan.csv')
w['freezing'] = w.MeanTempF.apply(lambda x: 1 if x < 32.0 else 0)
w['year'] = w.Date.apply(lambda x: x[:4])
w = w[['year','freezing']]
w.groupby('year').agg('sum').to_csv('freezing_year.csv')
"""s = 4.21
mean = 7.44
Z Score = 1.77
96.1636
"""
