#!/usr/bin/env python
import pandas as pd
import typing
from typing import List, Dict, Tuple, Optional
import matplotlib
import seaborn as sns

BULL_BIASED = 1 
CROWD = 0.75
BEAR_BIASED = 0


def save_df_as_image(df, path):
    # Set background to white
    norm = matplotlib.colors.Normalize(-1,1)
    colors = [[norm(-1.0), "white"],
            [norm( 1.0), "white"]]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    # Make plot
    plot = sns.heatmap(df, annot=True, cmap=cmap, cbar=False)
    plot.xaxis.tick_top()
    fig = plot.get_figure()
    fig.savefig(path)


# Computes the Brier score given the foreceast and actual values
def brier_score(forecast:float, actual:float) -> float:
    return 2 * (forecast - actual)**2

def question_score(forecast:float, actual:float) -> float:
    crowd_brier = brier_score(CROWD, actual)
    forecast_brier = brier_score(forecast, actual)
    return forecast_brier - crowd_brier

tickers = ['AAPL', 'GOOG', 'META','MSFT', 'NVDA', 'TSLA','BTC-USD']
tournament_years = ['2023', '2022', '2021', '2020', '2019']

participants = {'Bull': BULL_BIASED,'Crowd':CROWD, 'Bear': BEAR_BIASED }

stocks = {}

# Read in the data
for t in tickers:
    stocks[t] = pd.read_csv('{}.csv'.format(t))

# Filters the data to only January months
jans = lambda df: df[df['Date'].str.contains('-01-')]

# Makes a new column for the year
year = lambda df: df.assign(Year=df['Date'].str[:4])

# Keeps only the last 5 years of data
last_five = lambda df: df[df['Year'].isin(tournament_years)]

# Assigns a ticker column
ticker = lambda df, ticker: df.assign(Ticker=ticker)

consolidated = None
for t in tickers:
    stocks[t] = jans(stocks[t])
    stocks[t] = year(stocks[t])
    stocks[t] = last_five(stocks[t])
    stocks[t] = ticker(stocks[t], t)
    stocks[t] = stocks[t].groupby('Year').first()
    stocks[t] = stocks[t][['Ticker', 'Date', 'Adj Close']]
    stocks[t]['Change'] = stocks[t].shift(-1)['Adj Close'] / stocks[t]['Adj Close']
    stocks[t][t] = stocks[t]['Change'].apply(lambda x: 1 if x > 1 else 0)
    stocks[t] = stocks[t][[t]]
    stocks[t] = stocks[t].reset_index()
    if consolidated is None:
        consolidated = stocks[t]
    else:
        consolidated = consolidated.merge(stocks[t], on=['Year'])

# delete the last row since we don't have full data for 2023
consolidated = consolidated[:-1]

consolidated = consolidated.set_index('Year')

# Rename column BTC-USD to BTC
consolidated = consolidated.rename(columns={'BTC-USD': 'BTC'})

# transpose the data so that the years are the columns
consolidated = consolidated.transpose()

save_df_as_image(consolidated, 'consolidated.png')


callie_2019 = 7 * (question_score(.75, 1))
billy_2019 = 7 * (question_score(1, 1))
barry_2019 = 7 * (question_score(0, 1))
callie_2022 = 7 * (question_score(.75, 0))
billy_2022 = 7 * (question_score(1, 0))
barry_2022 = 7 * (question_score(0, 0))

print ('Callie 2019: {}'.format(callie_2019))
print ('Callie 2022: {}'.format(callie_2022))
print ('Callie all: {}'.format(3 *callie_2019 + callie_2022))
print ('Billy 2019: {}'.format(billy_2019))
print ('Billy 2022: {}'.format(billy_2022))
print ('Billy all: {}'.format(3*billy_2019 + billy_2022))
print ('Barry 2019: {}'.format(barry_2019))
print ('Barry 2022: {}'.format(barry_2022))
print ('Barry all: {}'.format(3*barry_2019 + barry_2022))

