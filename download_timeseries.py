#!/usr/bin/env python
# coding: utf-8

# # CDC: Monkeypox daily case totals

import pandas as pd
import us
import urllib.request, json
import datetime as dt

today = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%Y-%m-%d")
time = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%-I:%M %p")

## CDC Monkeypox
#### Aggregated by state

cases_url = 'https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/mpx_count_by_date.csv'

# with urllib.request.urlopen(cases_url) as url:
#     data = json.loads(url.read().decode())
#     cases_src = pd.DataFrame(data['data'])

cases_src = pd.read_csv(cases_url)

cases_src.columns = cases_src.columns.str.lower()

cases_src['cumulative_sum'] = cases_src['cases'].astype(int).cumsum()

cases_src.rename(columns={'epi-date': 'date'}, inplace=True)

## Exports

cases_src.to_csv(f'data/processed/monkeypox_cases_timeseries_cdc_{today}.csv', index=False)
cases_src.to_json(f'data/processed/monkeypox_cases_timeseries_cdc_{today}.json', orient='records', indent=4)

cases_src.to_csv(f'data/processed/monkeypox_cases_timeseries_cdc_latest.csv', index=False)
cases_src.to_json(f'data/processed/monkeypox_cases_timeseries_cdc_latest.json', orient='records', indent=4)