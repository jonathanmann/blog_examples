#!/usr/bin/env python
import pandas as pd
w = pd.read_csv('nyc_early_jan.csv')
w['freezing'] = w.MeanTempF.apply(lambda x: 1 if x < 32.0 else 0)
w['year'] = w.Date.apply(lambda x: x[:4])
w = w[['year','freezing']] #.reindex(index=w.index[::-1])
w.groupby('year').agg('sum').reset_index().iloc[::-1].to_json('freezing_year.json',orient='records')
