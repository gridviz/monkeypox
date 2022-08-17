#!/usr/bin/env python
# coding: utf-8

# CDC: Monkeypox cases, by country

import pandas as pd
import us
import urllib.request, json
import datetime as dt

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000

today = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%Y-%m-%d")
time = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%-I:%M %p")

## Country populations
#### Figures from World Bank

countries_pop = pd.read_csv('data/raw/countries_population.csv')

## CDC Monkeypox
#### Aggregated by country

countries_url = 'https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/MPX-Cases-Deaths-by-Country.csv'
countries_src = pd.read_csv(countries_url)

countries_src.columns = countries_src.columns.str.lower()

countries_src['updated_date'] = pd.to_datetime(countries_src['asof'].str.replace('Data as of ', '').str.replace(' 5:00 PM EDT', ''))

countries_src['hist_had'] = countries_src.category.str.replace('Has historically reported monkeypox', 'Has').str.replace('Has not historically reported monkeypox', 'Has not')

df = countries_src.drop(['category', 'asof'], axis=1).sort_values('cases', ascending=False)

## Merge
#### Population and cases to create a rate

merged_df = pd.merge(df, countries_pop, left_on='country', right_on='name')

merged_df['cases_per_million'] = ((merged_df['cases'] / merged_df['population'])*1000000).astype(float).round(2)

merged_df.drop(['name'], axis=1, inplace=True)

## Exports

merged_df.to_csv(f'data/processed/monkeypox_cases_countries_cdc_latest.csv', index=False)
merged_df.to_csv(f'data/processed/monkeypox_cases_countries_cdc_{today}.csv', index=False)
merged_df.to_json(f'data/processed/monkeypox_cases_countries_cdc_{today}.json', orient='records', indent=4)

