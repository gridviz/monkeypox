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
#### CDC only updates this weekly

cdc_timeseries = (
    pd.read_csv(
        "data/processed/monkeypox_cases_timeseries_cdc_latest.csv",
        parse_dates=["date"],
        names=["date", "cases", "asof", "cumulative_sum"],
        header=0,
    )
    .drop(["asof"], axis=1)
    .sort_values("date", ascending=False)
).reset_index(drop=True)

cdc_timeseries["date"] = pd.to_datetime(cdc_timeseries["date"]).dt.strftime("%Y-%m-%d")

#### The latest we have

historical_src = (
    pd.read_csv(
        "data/processed/monkeypox_cases_timeseries_cdc_historical.csv",
        parse_dates=["date"],
    )
    .sort_values("date", ascending=False)
    .reset_index(drop=True)
)

historical_src["date"] = pd.to_datetime(historical_src["date"]).dt.strftime("%Y-%m-%d")

historical_src = historical_src[historical_src['date'] < today].reset_index(drop=True)

## CDC Monkeypox
#### Latest totals, aggregated by state
states_src = pd.read_csv('https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/USmap_counts.csv')

states_src.columns = states_src.columns.str.lower().str.replace(' ', '_', regex=False)
states_src.drop(['case_range'], axis=1, inplace=True)
states_src['cases'] = states_src['cases'].astype(int)
states = states_src[(states_src['location'] != 'Total') & (states_src['location'] != 'Non-US Resident')].copy()

#### Aggregate totals among all states to add to timeseries
latest_total = states['cases'].sum()

historical_total = historical_src[historical_src["date"] == historical_src["date"].max()]["cumulative_sum"][0]

change = latest_total - historical_total

updated_data = {'date': today, 'cases': change, 'cumulative_sum': latest_total}

updated_data_df = pd.DataFrame(updated_data, index=[0])

updated_data_df["date"] = pd.to_datetime(updated_data_df["date"]).dt.strftime(
    "%Y-%m-%d"
)

df = (
    pd.concat([historical_src, updated_data_df])
    .drop_duplicates(subset="date")
    .sort_values("date", ascending=False)
    .copy()
)

## Exports
df.to_csv(f"data/processed/monkeypox_cases_timeseries_cdc_historical.csv", index=False)
df.to_csv(
    f"data/processed/monkeypox_cases_timeseries_cdc_historical_{today}.csv", index=False
)
df.to_csv(f"data/processed/monkeypox_cases_derived_timeseries_latest.csv", index=False)
df.to_json(
    f"data/processed/monkeypox_cases_derived_timeseries_latest.json",
    orient="records",
    indent=4,
)