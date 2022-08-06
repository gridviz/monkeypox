#!/usr/bin/env python
# coding: utf-8

# CDC: Monkeypox visualizations

import pandas as pd
import altair as alt
import altair_grid as altgrid
from altair_saver import save

alt.themes.register("grid", altgrid.theme)
alt.themes.enable("grid")
pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000
alt.data_transformers.disable_max_rows()
alt.renderers.enable("altair_saver", fmts=["vega-lite", "png"])

today = pd.Timestamp.now(tz="America/Los_Angeles").strftime("%Y-%m-%d")
time = pd.Timestamp.now(tz="America/Los_Angeles").strftime("%-I:%M %p")

## Cases timeseries

src = pd.read_csv(
    "https://raw.githubusercontent.com/gridviz/monkeypox/main/data/processed/monkeypox_cases_derived_timeseries_latest.csv"
)

src.head()

line = (
    alt.Chart(src)
    .mark_line()
    .encode(
        x=alt.X("date:T", axis=alt.Axis(tickCount=5), title=""),
        y=alt.Y("cumulative_sum:Q", title=" ", axis=alt.Axis(tickCount=5)),
    )
    .properties(title="Cumulative monkeypox cases in the U.S.", width=650, height=300)
    .configure_legend(symbolType="stroke", orient="top")
)

line.save("visuals/trendline_latest.png")
line.save(f"visuals/trendline_{today}.png")