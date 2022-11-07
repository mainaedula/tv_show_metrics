import streamlit as st
from vega_datasets import data
import altair as alt
import pandas as pd

st.header('Homework 2')

df = pd.read_csv('intention_by_show.csv', encoding="utf-16", sep='\t')

st.write(df.head())

shows = df['Show'].unique()
shows_selected = st.multiselect('Select shows', shows)


mask_shows = df['Show'].isin(shows_selected)

data = df[mask_shows]

bar = alt.Chart(data).mark_bar(color='#03cffc').encode(
    alt.X("Measure", title = "Intention"),
    y='Values',
    color='Measure',
    column='Show',
    tooltip = ['Measure', 'Values']
)

st.altair_chart(bar, use_container_width=True)