import streamlit as st
import plotly.express as px

# load data
data = px.data.gapminder()

# create scatter plot
fig = px.scatter(data, x="gdpPercap", y="lifeExp")

# add lasso select tool
fig.update_layout(
    {"dragmode": "select", "selectdirection": "h"},
    hovermode="closest",
    showlegend=False,
)

# show plot in streamlit
st.plotly_chart(fig)

# get selected data
selected_data = fig.data[0].selectedpoints

# show table of selected data
st.write(data.iloc[selected_data.point_inds])