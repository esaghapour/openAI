import random
import plotly.express as px  
import streamlit as st
import streamlit.components.v1 as components

_component_func = components.declare_component(
    "my_component",
    url="http://localhost:3001",
)

def my_component(fig):
    points = _component_func(spec=fig.to_json(), default=[], key="key")
    return points

@st.cache
def random_data():
    return random.sample(range(100), 50), random.sample(range(100), 50)

st.subheader("My Component")
x, y = random_data()
fig = px.scatter(x=x, y=y, title="My fancy plot")
v = my_component(fig)
st.write(v)
