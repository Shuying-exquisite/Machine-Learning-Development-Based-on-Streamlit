import streamlit as st

# 控制侧边栏内容的显示与隐藏
sidebar_visible = st.sidebar.checkbox('Show Sidebar', value=True)

if sidebar_visible:
    # 侧边栏显示内容
    st.sidebar.title("📊 Navigation")
    st.sidebar.radio("Choose slide:", ["Slide 1", "Slide 2", "Slide 3"])

# 主内容区域
st.title("Main Content Area")
st.write("This is the main content area of the app.")

if sidebar_visible:
    st.write("The sidebar is visible.")
else:
    st.write("The sidebar is hidden.")
