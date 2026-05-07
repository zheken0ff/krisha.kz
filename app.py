import streamlit as st
import pandas as pd

st.title("Krisha Dashboard")

df = pd.read_csv("cleaned_data.csv")

district = st.selectbox("Select district", df['district'].dropna().unique())

filtered = df[df['district'] == district]

st.write("Filtered data:")
st.dataframe(filtered.head())

st.write("Average price:", round(filtered['price'].mean(), 0))
st.write("Average price per m²:", round(filtered['price_per_m2'].mean(), 0))

st.line_chart(filtered.groupby('year')['price_per_m2'].mean())

# streamlit run app.py