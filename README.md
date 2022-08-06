# Tracking monkeypox cases in the U.S. and other countries

This repo tracks monkeypox virus case counts [released](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html) by the U.S. Centers for Disease Control and Prevention. 

It contains Python scripts that download and process [cases counts](https://github.com/gridviz/monkeypox/tree/main/data/processed) in the U.S. and countries around the world. For the U.S., Grid has created a running timeseries of case counts using historical data and daily state totals. 

Crude case rates in the U.S. tables were caluclated with 2020 population figures from the U.S. Census Bureau. For other countries, Grid has merged population data from the World Bank to create rates. 

### The following tables exist: 

| Table  | Formats | Update frequency | Source |
| ------------- | ------------- | ------------- | ------------- |
| **Latest U.S. state totals**  |  [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.json) | Daily | [CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html) |
| **Official U.S. timeseries totals**  | [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_timeseries_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_timeseries_cdc_latest.json) | Wednesdays | [CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/mpx-trends.html) |
| **Derived U.S. timeseries totals**  | [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_derived_timeseries_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_derived_timeseries_latest.json) | Daily | CDC/Grid |
| **Totals for 80+ countries**  | [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_countries_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_countries_cdc_latest.json) | Occasionally | [CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/world-map.html) |

The scripts run twice daily (at 6 a.m. and 6 p.m. Pacific time) via Github Actions. 

### Latest U.S. trend: 

![alt text](https://github.com/gridviz/monkeypox/raw/main/visuals/trendline_latest.png)

Questions? Comments? [Let us know](mailto:mstiles@grid.news). 
