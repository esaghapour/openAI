import streamlit as st
import pandas as pd
from sklearn.datasets import make_classification

# Create dummy data
data = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0, random_state=4)

# Convert data to Pandas dataframe
df = pd.DataFrame(data[0], columns=["x1", "x2"])
df["y"] = data[1]

# Add lasso selection tool
lasso = st.selectbox("Choose Lasso selection tool:", ["None", "Brush", "Lasso"])

# Plot scatter plot with lasso selection
if lasso == "Brush":
    st.brush_selector("Select points on the scatter plot", df, ["x1", "x2"], "y")
elif lasso == "Lasso":
    st.lasso_selector("Select points on the scatter plot", df, ["x1", "x2"], "y")
else:
    st.scatter_chart(df, "x1", "x2", "y")
