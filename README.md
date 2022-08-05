# Tracking U.S. monkeypox cases
This repo tracks monkeypox virus case counts [released](https://www.cdc.gov/poxvirus/monkeypox/response/2022/index.html) by the U.S. Centers for Disease Control &amp; Prevention. 

It contains two Python scripts that download and process [cases totals](https://github.com/gridviz/monkeypox/tree/main/data/processed) nationally and by state:

| Table  | Formats | CDC update frequency |
| ------------- | ------------- | ------------- |
| **Latest state totals**  |  [`csv`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_states_cdc_latest.json) | Daily |
| **Latest timeseries totals**  | [`csv`](https://github.com/gridviz/monkeypox/blob/main/data/processed/monkeypox_cases_timeseries_cdc_latest.csv), [`json`](https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_timeseries_cdc_latest.json) | Wednesdays |

The scripts run twice daily (at 6 a.m. and 6 p.m. Pacific time) via Github Actions. 

Questions? Comments? [Let us know](mailto:mstiles@grid.news). 
