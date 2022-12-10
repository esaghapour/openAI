import streamlit as st
import pandas as pd
import altair as alt
from sklearn.datasets import make_classification

# Create dummy data
data = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0, random_state=4)

# Convert data to Pandas dataframe
df = pd.DataFrame(data[0], columns=["x1", "x2"])
df["y"] = data[1]

# Add selection tool dropdown menu
selection_tool = st.selectbox("Choose selection tool:", ["None", "Brush", "Lasso"])

# Create scatter plot with selected selection tool
chart = alt.Chart(df).mark_circle().encode(
    x="x1",
    y="x2",
    color="y"
)

if selection_tool != "None":
    chart = chart.add_selection(
        alt.selection_interval(encodings=["x", "y"], bind="scales")
    )

st.altair_chart(chart, use_container_width=True)
