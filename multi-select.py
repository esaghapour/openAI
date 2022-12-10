import streamlit as st
import pandas as pd
import altair as alt

# Load the data into a Pandas DataFrame
data = pd.read_csv("data.csv")

# Create an Altair chart with the scatter plot
chart = alt.Chart(data).mark_point().encode(
    x="x",
    y="y"
)

# Add the lasso selection tool to the chart
chart = chart.add_selection(
    alt.selection_lasso()
)

# Display the chart in the Streamlit app
st.altair_chart(chart, use_container_width=True)

# Show a table of the data for the selected points
selected_data = alt.selection_data(data)
st.dataframe(selected_data)
