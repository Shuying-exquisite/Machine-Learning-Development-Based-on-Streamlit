import streamlit as st

# 创建标签页
tabs = st.tabs(["Home", "Analysis", "Settings"])

with tabs[0]:
    st.title("Home Page")
    st.write("Welcome to the Home Page! This is the main dashboard.")

with tabs[1]:
    st.title("Analysis Page")
    st.write("This page contains analysis and visualizations.")

with tabs[2]:
    st.title("Settings Page")
    st.write("Adjust your settings on this page.")
