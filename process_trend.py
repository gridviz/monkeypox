#!/usr/bin/env python
# coding: utf-8
# CDC: Monkeypox derived timeseries

import pandas as pd
import us
import urllib.request, json
import datetime as dt

today = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%Y-%m-%d")
time = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%-I:%M %p")

## Get historical case timeseries
#### May 17-Aug. 3
historical_src = pd.read_csv('data/processed/monkeypox_cases_timeseries_cdc_historical.csv', parse_dates=['date']).sort_values('date', ascending=False).reset_index(drop=True)
historical_src['date'] = historical_src['date'].astype(str)
historical_src = historical_src[historical_src['date'] < today].reset_index(drop=True)

## CDC Monkeypox
#### Latest totals, aggregated by state
states_url = 'https://www.cdc.gov/poxvirus/monkeypox/modules/data-viz/mpx_US_Total_databite.json'

with urllib.request.urlopen(states_url) as url:
    data = json.loads(url.read().decode())
    states_src = pd.DataFrame(data['data'])

states_src.columns = states_src.columns.str.lower().str.replace(' ', '_', regex=False)
states_src.drop(['case_range'], axis=1, inplace=True)
states_src['cases'] = states_src['cases'].astype(int)

states = states_src[(states_src['location'] != 'Total') & (states_src['location'] != 'Non-US Resident')].copy()

#### Aggregate totals among all states to add to timeseries
latest_total = states['cases'].sum()
historical_total = historical_src[historical_src['date'] == historical_src['date'].max()]['cumulative_sum'][0]
change = latest_total - historical_total
updated_data = {'date': today, 'cases': change, 'cumulative_sum': latest_total}
updated_data_df = pd.DataFrame(updated_data, index=[0])
df = pd.concat([updated_data_df, historical_src]).copy()

## Exports
df.to_csv(f'data/processed/monkeypox_cases_timeseries_cdc_historical.csv', index=False)
df.to_csv(f'data/processed/monkeypox_cases_derived_timeseries_latest.csv', index=False)
df.to_json(f'data/processed/monkeypox_cases_derived_timeseries_latest.json', orient='records', indent=4)