import streamlit as st

st.write("Red Blue States...")
import plotly.express as px

fig = px.bar(x = ["a", "b", "c"], y = [1, 3, 2])

st.plotly_chart(fig)

