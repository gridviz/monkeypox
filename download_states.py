#!/usr/bin/env python
# coding: utf-8

# CDC: Monkeypox cases, by state

import pandas as pd
import us
import urllib.request, json
import datetime as dt

today = dt.datetime.today().strftime("%Y-%m-%d")

## State populations
#### Figures from ACS 2020, 5-year estimates

states_pop = pd.read_csv('data/raw/states_population.csv')

#### Map FIPS codes to each state

states_pop['state_fips'] = states_pop['state'].map(us.states.mapping('name', 'fips'))

## CDC Monkeypox
#### Aggregated by state

states_url = 'https://www.cdc.gov/poxvirus/monkeypox/response/modules/MX-response-case-count-US.json'

with urllib.request.urlopen(states_url) as url:
    data = json.loads(url.read().decode())
    states_src = pd.DataFrame(data['data'])

states_src.columns = states_src.columns.str.lower()

#### Map FIPS codes and AP abbrevations to each state

states_src['state_fips'] = states_src['state'].map(us.states.mapping('name', 'fips'))
states_src['state_ap'] = states_src['state'].map(us.states.mapping('name', 'ap_abbr'))



## Merge
#### Population and cases to create a rate

df = pd.merge(states_src, states_pop, on=['state_fips', 'state'])

df['cases_per_million'] = ((df['cases'] / df['pop_acs_2020_5tr'])*1000000).astype(float).round(2)

df.drop(['range'], axis=1, inplace=True)


## Exports

df.to_csv(f'data/processed/monkeypox_cases_states_cdc_{today}.csv', index=False)
df.to_json(f'data/processed/monkeypox_cases_states_cdc_{today}.json', orient='records', indent=4)

df.to_csv(f'data/processed/monkeypox_cases_states_cdc_latest.csv', index=False)
df.to_json(f'data/processed/monkeypox_cases_states_cdc_latest.json', orient='records', indent=4)