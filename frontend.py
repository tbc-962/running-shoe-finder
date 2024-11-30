import streamlit as st
from backend import search_shoes_axesso

st.title("Find the Best Value Running Shoes")

niche = st.text_input("Enter the shoe niche (e.g., 'running shoes')", "running shoes")
min_price = st.number_input("Minimum Price ($)", min_value=0.0, value=0.0, step=0.01)
max_price = st.number_input("Maximum Price ($)", min_value=0.0, value=1000.0, step=0.01)
features = st.text_input("Specify features (comma-separated, e.g., 'lightweight, breathable')")

if st.button("Find Shoes"):
    with st.spinner("Searching..."):
        feature_list = [f.strip() for f in features.split(",") if f.strip()]
        result = search_shoes_axesso(niche, min_price, max_price, feature_list)
        if "error" in result:
            st.error(f"Error: {result['error']}")
        else:
            st.success("Found the best shoe!")
            st.json(result)
