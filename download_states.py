#!/usr/bin/env python
# coding: utf-8

# CDC: Monkeypox cases, by state

import pandas as pd
import us
import urllib.request, json
import datetime as dt

today = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%Y-%m-%d")
time = pd.Timestamp.now(tz='America/Los_Angeles').strftime("%-I:%M %p")

## State populations
#### Figures from ACS 2020, 5-year estimates

states_pop = pd.read_csv('data/raw/states_population.csv')

#### Map FIPS codes to each state

states_pop['state_fips'] = states_pop['state'].map(us.states.mapping('name', 'fips'))

## CDC Monkeypox
#### Aggregated by state

states_url = 'https://www.cdc.gov/poxvirus/monkeypox/modules/data-viz/mpx_US_Total_databite.json'

with urllib.request.urlopen(states_url) as url:
    data = json.loads(url.read().decode())
    states_src = pd.DataFrame(data['data'])

states_src.columns = states_src.columns.str.lower().str.replace(' ', '_', regex=False)

#### Map FIPS codes and AP abbrevations to each state

states_src['state_fips'] = states_src['location'].map(us.states.mapping('name', 'fips'))
states_src['state_ap'] = states_src['location'].map(us.states.mapping('name', 'ap_abbr'))
states_src['state_postal'] = states_src['location'].map(us.states.mapping('name', 'abbr'))

## Merge
#### Population and cases to create a rate

src = pd.merge(states_src, states_pop, on=['state_fips'])

df = src[(src['location'] != 'Total') | (src['location'] != 'Non-US Resident')].copy()

df['cases'] = df['cases'].astype(int)

df['cases_per_million'] = ((df['cases'] / df['pop_acs_2020_5tr'])*1000000).astype(float).round(2)
df['updated_date'] = today
df['updated_time'] = time

df['national_total'] = df['cases'].sum()

df.drop(['case_range'], axis=1, inplace=True)

## Exports

df.to_csv(f'data/processed/monkeypox_cases_states_cdc_{today}.csv', index=False)
df.to_json(f'data/processed/monkeypox_cases_states_cdc_{today}.json', orient='records', indent=4)

df.to_csv(f'data/processed/monkeypox_cases_states_cdc_latest.csv', index=False)
df.to_json(f'data/processed/monkeypox_cases_states_cdc_latest.json', orient='records', indent=4)