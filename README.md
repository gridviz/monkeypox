# Tracking U.S. monkeypox cases
This repo tracks monkeypox virus case counts [released](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html) by the U.S. Centers for Disease Control and Prevention. 

It contains Python scripts that download and process [cases totals](https://github.com/gridviz/monkeypox/tree/main/data/processed) nationally and by state. Because the CDC only updates its timeseries weekly, Grid has also derived a running daily case count from historical data and daily state totals.  

| Table  | Formats | Update frequency | Source |
| ------------- | ------------- | ------------- | ------------- |
| **Latest state totals**  |  [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.json) | Daily | [CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html) |
| **Official timeseries totals**  | [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_timeseries_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_timeseries_cdc_latest.json) | Wednesdays | [CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/mpx-trends.html) |
| **Derived timeseries totals**  | [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_derived_timeseries_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_derived_timeseries_latest.json) | Daily | CDC/Grid |

The scripts run twice daily (at 6 a.m. and 6 p.m. Pacific time) via Github Actions. 

Questions? Comments? [Let us know](mailto:mstiles@grid.news). 
